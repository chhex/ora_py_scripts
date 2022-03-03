CFLAGS="-I$(brew86 --prefix openssl)/include -I$(brew86 --prefix readline)/include" \
LDFLAGS="-L$(brew86 --prefix openssl)/lib -L$(brew86 --prefix readline)/lib" \
VERSION_ALIAS="3.8.1_x86" \
pyenv86 install -v 3.8.1
