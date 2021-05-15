# Lemon Router

An anonymized browser, thanks to the implementation of the Tor proxy. It allows the creation of a hidden service on the Tor network (in .onion) as well as the indexing of this one with an updated file and shared in peer-to-peer in real time.



**DISCLAIMER: THIS PROJECT IS FOR ACADEMIC PURPOSES ONLY. THE DEVELOPERS TAKE NO RESPONSIBILITY FOR ILLEGAL USAGE AND/OR POTENTIAL HARMS.**

## Requirements

- Python >= 3
  - PyQt5
  - PyQt5-sip
  - PyQtWebEngine
- Tor proxy
- Nginx

## Features

- [x] Graphic interface
- [ ] Proxy through Tor
- [x] Hidden service self-hosted
- [ ] Indexing of hidden services
- [ ] Monitoring tool

## Installation (development)

### Linux :

#### Install requirements

#### Ubuntu & Debian :

##### 1. Get Python >= 3

> --> https://www.python.org/

```shell
~# sudo apt-get install python3
```

#### Ubuntu :

##### 2. Get Nginx

> --> https://nginx.org/

```shell
~# sudo apt install curl gnupg2 ca-certificates lsb-release
~# echo "deb http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
~# echo "deb http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
~# echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
~# curl -o /tmp/nginx_signing.key https://nginx.org/keys/nginx_signing.key
~# gpg --dry-run --quiet --import --import-options show-only /tmp/nginx_signing.key
~# gpg --with-fingerprint /tmp/nginx_signing.key #for ubuntu 16.04
~# sudo mv /tmp/nginx_signing.key /etc/apt/trusted.gpg.d/nginx_signing.asc
~# sudo apt-get update
~# sudo apt-get install nginx
```

#### Debian :

##### 2. Get Nginx

> --> https://nginx.org/

```shell
~# sudo apt install curl gnupg2 ca-certificates lsb-release
~# echo "deb http://nginx.org/packages/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
~# echo "deb http://nginx.org/packages/mainline/debian `lsb_release -cs` nginx" \
    | sudo tee /etc/apt/sources.list.d/nginx.list
~# echo -e "Package: *\nPin: origin nginx.org\nPin: release o=nginx\nPin-Priority: 900\n" \
    | sudo tee /etc/apt/preferences.d/99nginx
~# curl -o /tmp/nginx_signing.key https://nginx.org/keys/nginx_signing.key
~# gpg --dry-run --quiet --import --import-options import-show /tmp/nginx_signing.key
~# sudo mv /tmp/nginx_signing.key /etc/apt/trusted.gpg.d/nginx_signing.asc
~# sudo apt-get update
~# sudo apt-get install nginx
```

#### Ubuntu & Debian :

##### 3. Get Tor Proxy

> --> https://torproject.org

```shell
~# sudo apt-get install tor
```



#### Setting up the environment

##### 1. Clone this project

You can use git to clone this project or download .zip file from GitHub repository.

```shell
~# git clone https://github.com/decentralizeme/lemonrouter.git
~# cd lemonrouter/
```

##### 2. Configure and install dependencies

```shell
~# cd platform/linux
~# chmod +x main
~# ./main
```

#### Usage

##### Concept explanations:

The Lemon Router networks use the [peer-to-peer](https://en.wikipedia.org/wiki/Peer-to-peer) protocol to share a common file with each client which will serve as their [DNS resolver](https://en.wikipedia.org/wiki/Domain_Name_System). This file is updated each time a hidden service is created via the Lemon Router client. The addresses are generated thanks to the implementation of [Tor ](https://en.wikipedia.org/wiki/Tor_(anonymity_network)) (ipv4 or ipv6 ending in .onion), the navigation is completely anonymous and allows [access to hidden services](https://en.wikipedia.org/wiki/The_Hidden_Wiki) as well as their indexing.

Peers: ...

Nodes: ...

##### 1. Start browsing

```shell
~# cd lemonrouter/platform/linux
~# ./main
```

##### 2. Create an hidden service

```shell
#soon
```

##### 3. Index your hidden service

```shell
#soon
```

##### 4. Monitor your hidden service

```shell
#soon
```

## Contributing

Bug reports and pull requests are welcome on GitHub repository at https://github.com/decentralizeme/lemonrouter. This project is intended to be a safe and welcoming space for collaboration, and contributors must adhere to the [contributors code of conduct](https://www.contributor-covenant.org/).

#### - Code modification

1. Open a [Pull request](https://github.com/decentralizeme/lemonrouter/pulls)
2. Make sure all CI tests pass
3. Wait for the code to be revised
4. Publish the new version of the code

#### - Conception and development

1. As few dependencies as possible
2. No build script needed
3. Easy and simple graphical experience
4. Readable code and commented if possible
5. Fewer external calls slowing down the software
6. Easy-to-navigate on the clearnet, deep web and darknet

## Licence

[BSD-3-Clause License](https://github.com/decentralizeme/lemonrouter/blob/main/LICENSE) > open-source