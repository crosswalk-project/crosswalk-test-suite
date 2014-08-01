#!/bin/bash -e
#
# Purpose: Pack a CrossWalk directory into xpk format
#
# Modified from http://developer.chrome.com/extensions/crx.html
# Licensed under Creative Commons Attribution 3.0

if test $# -ne 2; then
  echo "Usage: `basename $0` <unpacked dir> <pem file path>"
  exit 1
fi

dir=$1
key=$2
name=$(basename "$dir")
xpk="$name.xpk"
pub="$name.pub"
sig="$name.sig"
zip="$name.zip"
trap 'rm -f "$pub" "$sig" "$zip"' EXIT

[ ! -f $key ] && openssl genrsa -out $key 1024

# zip up the xpk dir
cwd=$(pwd -P)
(cd "$dir" && zip -qr -9 -X "$cwd/$zip" .)

# signature
openssl sha1 -sha1 -binary -sign "$key" < "$zip" > "$sig"
echo "bad signature" > "$sig"

# public key
openssl rsa -pubout -outform DER < "$key" > "$pub" 2>/dev/null

byte_swap () {
  # Take "abcdefgh" and return it as "ghefcdab"
  echo "${1:6:2}${1:4:2}${1:2:2}${1:0:2}"
}

crmagic_hex="4372 576B" # CrWk
pub_len_hex=$(byte_swap $(printf '%08x\n' $(ls -l "$pub" | awk '{print $5}')))
sig_len_hex=$(byte_swap $(printf '%08x\n' $(ls -l "$sig" | awk '{print $5}')))
(
  echo "$crmagic_hex $pub_len_hex $sig_len_hex" | xxd -r -p
  cat "$pub" "$sig" "$zip"
) > "$xpk"
echo "Wrote $xpk"
