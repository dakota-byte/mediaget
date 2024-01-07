#!/bin/bash



# Check if no arguments are provided

if [ $# -eq 0 ]; then

  echo "Usage: $0 [-t <parameter>] [-i <parameter>] [-y <parameter>]"

  echo "-t   : tiktok"

  echo "-i   : instagram"

  echo "-y   : youtube"

  exit 1

fi



while getopts ":t:i:y:" opt; do

  case $opt in

    t)

      # tiktok

      python ./dget_tiktok.py "$OPTARG"

      exit 0

      ;;

    i)

      # insta

      python ./dget_instagram.py "$OPTARG"

      exit 0

      ;;

    y)

      # youtube

      python ./dget_youtube.py "$OPTARG"

      exit 0

      ;;

    \?)

      echo "Invalid option: -$OPTARG" >&2

      exit 1

      ;;

  esac

done

