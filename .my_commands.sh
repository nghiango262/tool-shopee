#!/bin/zsh

function create() {
    source .env
    python create.py $1
    cd $FILEPATH$1
    
}

function shopee() {
    source .env
    python run_shopee.py
    echo "SHOPEE---SHOPEE---SHOPEE"
}
