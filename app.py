from flask import Flask, render_template_string
import socket

app = Flask(__name__)

# HTML Template with Pixelated Flying Bat
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ hostname }}</title>
    <style>
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden;
        }

        .hostname {
            font-size: 3rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
            margin-bottom: 50px;
        }

        .bat-container {
            position: relative;
            width: 600px;
            height: 200px;
        }

        .bat {
            position: absolute;
            width: 64px;
            height: 32px;
            animation: bat-fly 4s linear infinite;
            image-rendering: pixelated;
            image-rendering: -moz-crisp-edges;
            image-rendering: crisp-edges;
        }

        .bat::before {
            content: '';
            position: absolute;
            width: 64px;
            height: 32px;
            background-image: 
                /* Bat sprite frame 1 - wings up */
                radial-gradient(circle at 8px 16px, #333 2px, transparent 2px),
                radial-gradient(circle at 16px 8px, #333 4px, transparent 4px),
                radial-gradient(circle at 32px 4px, #333 3px, transparent 3px),
                radial-gradient(circle at 48px 8px, #333 4px, transparent 4px),
                radial-gradient(circle at 56px 16px, #333 2px, transparent 2px),
                /* Body */
                linear-gradient(to bottom, #666 24px, #444 32px),
                /* Wings */
                linear-gradient(45deg, #555 0%, #333 50%, #222 100%),
                linear-gradient(-45deg, #555 0%, #333 50%, #222 100%);
            background-size: 
                4px 4px, 8px 8px, 6px 6px, 8px 8px, 4px 4px,
                8px 32px, 28px 20px, 28px 20px;
            background-position: 
                0px 12px, 4px 0px, 28px -2px, 52px 0px, 60px 12px,
                28px 0px, 0px 8px, 36px 8px;
            background-repeat: no-repeat;
            animation: bat-wing-flap 0.3s ease-in-out infinite alternate;
        }

        /* Alternative bat sprite using CSS pixel art */
        .bat-pixel {
            position: absolute;
            width: 80px;
            height: 40px;
            animation: bat-fly 4s linear infinite;
        }

        .bat-pixel::before {
            content: '';
            position: absolute;
            width: 80px;
            height: 40px;
            background-image: 
                /* Creating a detailed pixel bat */
                linear-gradient(to right, transparent 36px, #666 36px, #666 44px, transparent 44px),
                linear-gradient(to right, transparent 34px, #555 34px, #555 38px, transparent 38px, transparent 42px, #555 42px, #555 46px, transparent 46px),
                linear-gradient(to right, transparent 32px, #444 32px, #444 36px, transparent 36px, transparent 44px, #444 44px, #444 48px, transparent 48px),
                linear-gradient(to right, transparent 28px, #333 28px, #333 32px, transparent 32px, transparent 48px, #333 48px, #333 52px, transparent 52px),
                linear-gradient(to right, transparent 24px, #444 24px, #444 28px, transparent 28px, transparent 52px, #444 52px, #444 56px, transparent 56px),
                linear-gradient(to right, transparent 20px, #555 20px, #555 24px, transparent 24px, transparent 56px, #555 56px, #555 60px, transparent 60px),
                linear-gradient(to right, transparent 16px, #333 16px, #333 20px, transparent 20px, transparent 60px, #333 60px, #333 64px, transparent 64px),
                linear-gradient(to right, transparent 12px, #444 12px, #444 16px, transparent 16px, transparent 64px, #444 64px, #444 68px, transparent 68px),
                linear-gradient(to right, transparent 8px, #555 8px, #555 12px, transparent 12px, transparent 68px, #555 68px, #555 72px, transparent 72px),
                linear-gradient(to right, transparent 4px, #333 4px, #333 8px, transparent 8px, transparent 72px, #333 72px, #333 76px, transparent 76px),
                linear-gradient(to right, transparent 0px, #444 0px, #444 4px, transparent 4px, transparent 76px, #444 76px, #444 80px, transparent 80px);
            background-size: 80px 2px;
            background-position: 
                0px 18px, 0px 16px, 0px 14px, 0px 12px, 0px 10px,
                0px 8px, 0px 6px, 0px 4px, 0px 2px, 0px 0px, 0px 20px;
            background-repeat: no-repeat;
            animation: bat-wing-flap 0.4s ease-in-out infinite alternate;
        }

        @keyframes bat-fly {
            0% {
                left: -80px;
                top: 50%;
                transform: translateY(-50%);
            }
            25% {
                top: 30%;
                transform: translateY(-50%) rotate(-5deg);
            }
            50% {
                top: 70%;
                transform: translateY(-50%) rotate(5deg);
            }
            75% {
                top: 40%;
                transform: translateY(-50%) rotate(-3deg);
            }
            100% {
                left: 600px;
                top: 60%;
                transform: translateY(-50%);
            }
        }

        @keyframes bat-wing-flap {
            0% {
                transform: scaleY(0.8);
                filter: brightness(0.8);
            }
            100% {
                transform: scaleY(1.2);
                filter: brightness(1.2);
            }
        }

        .moon {
            position: absolute;
            top: 50px;
            right: 100px;
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #fff 0%, #f0f0f0 50%, #ddd 100%);
            border-radius: 50%;
            box-shadow: 0 0 20px rgba(255,255,255,0.3);
        }

        .moon::before {
            content: '';
            position: absolute;
            width: 12px;
            height: 12px;
            background: #ccc;
            border-radius: 50%;
            top: 20px;
            left: 25px;
            box-shadow: 
                15px 10px 0 -2px #ccc,
                8px 35px 0 -4px #ccc,
                35px 25px 0 -3px #ccc;
        }

        .stars {
            position: absolute;
            width: 100%;
            height: 100%;
            pointer-events: none;
        }

        .star {
            position: absolute;
            color: #fff;
            font-size: 16px;
            animation: twinkle 2s ease-in-out infinite alternate;
        }

        @keyframes twinkle {
            0% { opacity: 0.3; transform: scale(0.8); }
            100% { opacity: 1; transform: scale(1.2); }
        }

        .star:nth-child(1) { top: 20%; left: 15%; animation-delay: 0s; }
        .star:nth-child(2) { top: 30%; left: 80%; animation-delay: 0.5s; }
        .star:nth-child(3) { top: 60%; left: 20%; animation-delay: 1s; }
        .star:nth-child(4) { top: 15%; left: 60%; animation-delay: 1.5s; }
        .star:nth-child(5) { top: 70%; left: 75%; animation-delay: 2s; }
        .star:nth-child(6) { top: 45%; left: 10%; animation-delay: 0.3s; }
        .star:nth-child(7) { top: 25%; left: 40%; animation-delay: 1.2s; }
        .star:nth-child(8) { top: 80%; left: 50%; animation-delay: 0.8s; }

        .ground {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 40px;
            background: linear-gradient(to top, #111 0%, #222 50%, transparent 100%);
        }
    </style>
</head>
<body>
    <div class="hostname">{{ hostname }}</div>
    
    <div class="bat-container">
        <div class="moon"></div>
        <div class="bat-pixel"></div>
        <div class="stars">
            <div class="star">✦</div>
            <div class="star">✧</div>
            <div class="star">⭐</div>
            <div class="star">✦</div>
            <div class="star">✧</div>
            <div class="star">✦</div>
            <div class="star">✧</div>
            <div class="star">⭐</div>
        </div>
        <div class="ground"></div>
    </div>
</body>
</html>
'''

@app.route("/")
def home():
    """Main route showing hostname with flying pixelated bat animation"""
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, hostname=hostname)

@app.route("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)