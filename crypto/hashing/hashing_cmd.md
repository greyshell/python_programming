
# list of openssl supported algorithms
openssl dgst -list

# md5
echo -n "hello world" | openssl dgst -md5  # hex format (default)
echo -n "hello world" | md5sum
echo -n "hello world" | md5deep
md5sum msg.txt
md5deep msg.txt
# display in base64 format
echo -n "hello world" | openssl dgst -md5 -binary | openssl enc -base64

# sha1
echo -n "hello world" | openssl dgst -sha1
echo -n "hello world" | sha1sum
echo -n "hello world" | sha1deep
sha1sum msg.txt
sha1deep msg.txt

# sha2
echo -n "hello world" | openssl dgst -sha256
echo -n "hello world" | sha256sum
echo -n "hello world" | sha256deep
sha256sum msg.txt
sha256deep msg.txt

# sha3
echo -n "hello world" | openssl dgst -sha3-512
openssl dgst -sha3-512 msg.txt

# shake256
# default XOF=32
echo -n "hello world" | openssl dgst -shake256 -xoflen 64 

 