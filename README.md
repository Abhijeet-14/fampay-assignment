# fampay-assignment

# Run Applicaiton

## Build Image

    docker build -t fampay_assign:latest -t fampay_assign:v1 .

## Run Continaer

    docker run --name fampay_assign_container -d -p 8000:8000 fampay_assign:latest
