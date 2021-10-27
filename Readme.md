# Marketplayz 
## Summary
The system exposes data of games & gamers,  
using fastapi (which includes flask & swagger).

## How to run:
1. For local run:
<br>
    pip install -r requirements.txt
<br>
    python main.py
2. Run using docker:
<br>
    docker build . -t marketplayz
<br>
    docker run marketplayz -p 8080:8080