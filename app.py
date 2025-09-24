from flask import Flask, render_template_string
import socket

app = Flask(__name__)

# HTML Template with White Pixel Bat on Black Background
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
            text-shadow: 2px 2px 4px rgba(255,255,255,0.3);
            margin-bottom: 50px;
            z-index: 10;
            position: relative;
        }

        .bat-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
        }

        .bat {
            width: 1px;
            height: 1px;
            transform: scale(3);
            position: absolute;
            left: 50px;
            top: 50px;
            animation: bat 0.4s steps(1) infinite, fly-around 20s linear infinite;
            image-rendering: pixelated;
            image-rendering: -moz-crisp-edges;
            image-rendering: crisp-edges;
        }

        @keyframes fly-around {
            0% { 
                left: 50px; 
                top: 100px; 
                transform: scale(3) rotate(0deg);
            }
            25% { 
                left: calc(100vw - 300px); 
                top: 200px; 
                transform: scale(3) rotate(15deg);
            }
            50% { 
                left: calc(100vw - 200px); 
                top: calc(100vh - 300px); 
                transform: scale(3) rotate(-10deg);
            }
            75% { 
                left: 100px; 
                top: calc(100vh - 200px); 
                transform: scale(3) rotate(5deg);
            }
            100% { 
                left: 50px; 
                top: 100px; 
                transform: scale(3) rotate(0deg);
            }
        }

        /* Bat animation keyframes with white pixels */
        @keyframes bat {
            0% {
                box-shadow: 33px 6px #ffffff, 34px 6px #ffffff, 35px 6px #ffffff, 36px 6px #ffffff, 20px 7px #ffffff, 21px 7px #ffffff, 22px 7px #ffffff, 23px 7px #ffffff, 33px 7px #ffffff, 34px 7px #ffffff, 35px 7px #000000, 36px 7px #000000, 37px 7px #ffffff, 38px 7px #ffffff, 39px 7px #ffffff, 43px 7px #ffffff, 20px 8px #ffffff, 21px 8px #ffffff, 22px 8px #ffffff, 23px 8px #ffffff, 33px 8px #ffffff, 34px 8px #ffffff, 35px 8px #000000, 36px 8px #000000, 37px 8px #ffffff, 38px 8px #ffffff, 39px 8px #ffffff, 43px 8px #ffffff, 17px 9px #ffffff, 18px 9px #ffffff, 19px 9px #ffffff, 20px 9px #ffffff, 35px 9px #ffffff, 36px 9px #000000, 37px 9px #000000, 38px 9px #000000, 39px 9px #000000, 40px 9px #ffffff, 41px 9px #ffffff, 42px 9px #ffffff, 43px 9px #000000, 44px 9px #ffffff, 45px 9px #ffffff, 16px 10px #ffffff, 17px 10px #000000, 18px 10px #000000, 19px 10px #000000, 20px 10px #ffffff, 36px 10px #ffffff, 37px 10px #000000, 38px 10px #000000, 39px 10px #000000, 40px 10px #000000, 41px 10px #000000, 42px 10px #000000, 43px 10px #000000, 44px 10px #ffffff, 45px 10px #ffffff, 16px 11px #ffffff, 17px 11px #000000, 18px 11px #000000, 19px 11px #000000, 20px 11px #ffffff, 36px 11px #ffffff, 37px 11px #000000, 38px 11px #000000, 39px 11px #000000, 40px 11px #000000, 41px 11px #000000, 42px 11px #000000, 43px 11px #000000, 44px 11px #ffffff, 45px 11px #ffffff, 13px 12px #ffffff, 14px 12px #ffffff, 15px 12px #ffffff, 16px 12px #000000, 17px 12px #000000, 18px 12px #ffffff, 19px 12px #ffffff, 20px 12px #ffffff, 36px 12px #ffffff, 37px 12px #ffffff, 38px 12px #ffffff, 39px 12px #000000, 40px 12px #000000, 41px 12px #000000, 42px 12px #000000, 43px 12px #000000, 44px 12px #ffffff, 45px 12px #ffffff, 12px 13px #ffffff, 13px 13px #000000, 14px 13px #000000, 15px 13px #000000, 16px 13px #000000, 17px 13px #000000, 18px 13px #ffffff, 19px 13px #ffffff, 37px 13px #ffffff, 38px 13px #ffffff, 39px 13px #000000, 40px 13px #000000, 41px 13px #000000, 42px 13px #000000, 43px 13px #000000, 44px 13px #000000, 45px 13px #000000, 46px 13px #ffffff, 10px 14px #ffffff, 11px 14px #ffffff, 12px 14px #000000, 13px 14px #000000, 14px 14px #000000, 15px 14px #000000, 16px 14px #000000, 17px 14px #ffffff, 36px 14px #ffffff, 37px 14px #ffffff, 38px 14px #ffffff, 39px 14px #000000, 40px 14px #000000, 41px 14px #000000, 42px 14px #000000, 43px 14px #000000, 44px 14px #000000, 45px 14px #000000, 46px 14px #000000, 47px 14px #ffffff, 10px 15px #ffffff, 11px 15px #ffffff, 12px 15px #000000, 13px 15px #000000, 14px 15px #000000, 15px 15px #000000, 16px 15px #000000, 17px 15px #ffffff, 36px 15px #ffffff, 37px 15px #ffffff, 38px 15px #ffffff, 39px 15px #000000, 40px 15px #000000, 41px 15px #000000, 42px 15px #000000, 43px 15px #000000, 44px 15px #000000, 45px 15px #000000, 46px 15px #000000, 47px 15px #ffffff;
            }
            25% {
                box-shadow: 17px 7px #ffffff, 37px 7px #ffffff, 38px 7px #ffffff, 17px 8px #ffffff, 37px 8px #ffffff, 38px 8px #ffffff, 16px 9px #ffffff, 17px 9px #000000, 18px 9px #ffffff, 19px 9px #ffffff, 36px 9px #ffffff, 37px 9px #000000, 38px 9px #000000, 39px 9px #ffffff, 43px 9px #ffffff, 44px 9px #ffffff, 45px 9px #ffffff, 14px 10px #ffffff, 15px 10px #ffffff, 16px 10px #000000, 17px 10px #ffffff, 37px 10px #ffffff, 38px 10px #ffffff, 39px 10px #000000, 40px 10px #ffffff, 43px 10px #ffffff, 44px 10px #000000, 45px 10px #000000, 46px 10px #ffffff, 14px 11px #ffffff, 15px 11px #ffffff, 16px 11px #000000, 17px 11px #ffffff, 37px 11px #ffffff, 38px 11px #ffffff, 39px 11px #000000, 40px 11px #ffffff, 43px 11px #ffffff, 44px 11px #000000, 45px 11px #000000, 46px 11px #ffffff, 10px 12px #ffffff, 11px 12px #ffffff, 13px 12px #ffffff, 14px 12px #000000, 15px 12px #000000, 16px 12px #000000, 17px 12px #ffffff, 37px 12px #ffffff, 38px 12px #ffffff, 39px 12px #000000, 40px 12px #000000, 41px 12px #ffffff, 42px 12px #ffffff, 43px 12px #ffffff, 44px 12px #000000, 45px 12px #000000, 46px 12px #000000, 47px 12px #ffffff;
            }
            50% {
                box-shadow: 47px 14px #000000, 47px 15px #000000, 14px 16px #000000, 15px 16px #000000, 28px 20px #ffffff, 29px 20px #ffffff, 30px 20px #ffffff, 48px 20px #000000, 49px 20px #000000, 9px 21px #000000, 18px 21px #ffffff, 19px 21px #ffffff, 20px 21px #ffffff, 21px 21px #ffffff, 22px 21px #ffffff, 23px 21px #ffffff, 27px 21px #ffffff, 28px 21px #000000, 29px 21px #ffffff, 30px 21px #ffffff, 20px 22px #ffffff, 21px 22px #000000, 22px 22px #000000, 23px 22px #000000, 24px 22px #ffffff, 25px 22px #ffffff, 26px 22px #ffffff, 27px 22px #ffffff, 28px 22px #000000, 29px 22px #000000, 30px 22px #000000, 31px 22px #ffffff;
            }
            75% {
                box-shadow: 31px 16px #ffffff, 32px 16px #ffffff, 31px 17px #ffffff, 32px 17px #ffffff, 20px 18px #ffffff, 21px 18px #ffffff, 28px 18px #ffffff, 29px 18px #ffffff, 30px 18px #ffffff, 31px 18px #000000, 32px 18px #000000, 33px 18px #ffffff, 34px 18px #ffffff, 20px 19px #ffffff, 21px 19px #ffffff, 28px 19px #ffffff, 29px 19px #ffffff, 30px 19px #ffffff, 31px 19px #000000, 32px 19px #000000, 33px 19px #ffffff, 34px 19px #ffffff, 20px 20px #ffffff, 21px 20px #000000, 22px 20px #ffffff, 23px 20px #ffffff, 27px 20px #ffffff, 28px 20px #000000, 29px 20px #ffffff, 30px 20px #ffffff, 31px 20px #000000, 32px 20px #000000, 33px 20px #ffffff, 34px 20px #ffffff;
            }
        }

        /* Additional decorative elements */
        .star {
            position: absolute;
            color: #fff;
            font-size: 12px;
            animation: twinkle 3s ease-in-out infinite alternate;
        }

        @keyframes twinkle {
            0% { opacity: 0.3; }
            100% { opacity: 1; }
        }

        .star:nth-child(1) { top: 10%; left: 10%; animation-delay: 0s; }
        .star:nth-child(2) { top: 20%; left: 80%; animation-delay: 1s; }
        .star:nth-child(3) { top: 70%; left: 15%; animation-delay: 2s; }
        .star:nth-child(4) { top: 15%; left: 70%; animation-delay: 0.5s; }
        .star:nth-child(5) { top: 80%; left: 85%; animation-delay: 1.5s; }
    </style>
</head>
<body>
    <div class="hostname">{{ hostname }}</div>
    
    <div class="bat-container">
        <div class="bat"></div>
        <div class="star">✦</div>
        <div class="star">✧</div>
        <div class="star">⭐</div>
        <div class="star">✦</div>
        <div class="star">✧</div>
    </div>
</body>
</html>
'''

@app.route("/")
def home():
    """Main route showing hostname with flying white pixel bat on black background"""
    hostname = socket.gethostname()
    return render_template_string(HTML_TEMPLATE, hostname=hostname)

@app.route("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)