echo "change apt source to ZJU source"
sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak
sudo cp sources.list /etc/apt/sources.list
sudo apt-get update
sudo apt-get upgrade

echo "install curl wget git zsh vim openssh-server guake dconf-tools"
sudo apt install -y curl wget git zsh vim openssh-server guake dconf-tools

# install powerline fonts
# clone
git clone https://github.com/powerline/fonts.git --depth=1
# install
cd fonts
./install.sh
# clean-up a bit
cd ..
rm -rf fonts

sudo apt autoremove -y

# install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
