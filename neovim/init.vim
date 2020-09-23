set nocompatible

" Use system clipboard
set clipboard+=unnamedplus

filetype plugin on

syntax on

" Vertically center document when entering insert mode
autocmd InsertEnter * norm zz

" Color
set background = "dark"
colorscheme ron

set encoding=utf-8
set relativenumber
set nohlsearch
set hidden
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set scrolloff=8
set noshowmode
