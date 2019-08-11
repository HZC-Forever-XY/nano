## Setup

Ubuntu 装机之后自动安装软件的脚本，使用如下命令为脚本添加运行权限，并运行脚本

```bash
sudo chmod a+x *.sh
./setup.sh
```

上面的命令运行结束后仍需运行

```
# install zsh-autosuggestions zsh-syntax-highlighting
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
echo "source $ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```

脚本会将 apt 源换为浙大源并更新一次所有软件，此动作需要确认，可输入 n 取消

脚本会安装 curl wget git zsh vim openssh-server guake 等工具，中途会询问是否要将 shell 换为 zsh，输入 y 之后换用 zsh shell，之后运行第二块命令

脚本运行结束之后，你还应该做以下事情：

* 关闭默认终端，使用 guake 终端

* 在 .zshrc 文件中将 ZSH_THEME=“agnoster” 改为

  ```bash
  ZSH_THEME="agnoster"
  ```

* 在 .zshrc 文件中将 plugins=(git) 改为如下

  ```bash
  plugins=(
    git
    zsh-autosuggestions
  )
  ```

* 打开 dconf-tools 的 org > gnome > desktop > terminal 选择 guake 为默认终端

  > 可能不存在这个路径，便不再配置

* 修改 guake 终端配置如下：

  #### General ####

  * 取消 Enable popup notifications on startup

  #### Main Window ####

  * 取消 show tab bar

  #### Scrollbar ####

  * 选中 infinite scrolling

  #### Appearance ####

  * 取消 Use the system fixed width font
  * 选择 Source Code Pro for Powerline light 14pt
  * 选择 I-Beam Cursor shape
  * 选择 Solaried Dark Higher Contrast built-in schemes

  #### Keyboard Shortcut ####

  * 设置 Toggle Guake visibility 快捷键为 Ctrl+Shift+Space

  #### 设置开机启动 ####

  * 在启动应用程序中添加命令 /usr/bin/guake

  #### 默认 shell ####

  * 如果 Guake 的默认 shell 还是 bash，可以在 Shell 中手动将其修改为 /usr/bin/zsh

* 如果你在重启了终端之后，自动提示的颜色还是过浅，可运行如下命令，之后重新打开终端即可

```bash
mv $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh.bak
cp zsh-autosuggestions.zsh $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
```

之后可运行

```
./setup_ros.sh
```

脚本安装 ros，同样有一次提示询问是否要更新一次软件，可自行选择

Ubuntu 虚拟机可以使用宿主机的代理设置只需要

* 在 .zshrc 文件中添加下面两行中的一行，推荐使用 http

  ```
  export all_proxy=http://<宿主机 IP>:<宿主机 http 代理监听端口>
  export all_proxy=socks5://<宿主机 IP>:<宿主机 socks5 代理监听端口>
  ```

* 在系统设置中添加手动代理 http、https、sock 主机均添

* ```
   export all_proxy=http://<宿主机 IP>:<宿主机 http 代理监听端口>
   export all_proxy=socks5://<宿主机 IP>:<宿主机 socks5 代理监听端口>
  ```

* 在系统设置中添加手动代理 http、https、sock 主机均填宿主机 IP，端口http 与 https 填 http 端口，sock 主机填 socks5 端口



