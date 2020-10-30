set nocompatible
set hidden
set noshowmode

let mapleader=" "
let maplocalleader=" "
" set spellfile="/home/silas/.local/share/nvim/site/spell/en.utf-8.spl"
" set spellfile="/usr/share/dict/words"

cmap Ww w !sudo tee > /dev/null %
cmap Q q!

" command <Wq> <:w !sudo tee %>

call plug#begin('~/.local/share/nvim/plugged')

Plug 'itchyny/lightline.vim'
Plug 'tpope/vim-surround'
Plug 'tpope/vim-repeat'
Plug 'junegunn/goyo.vim'
Plug 'jreybert/vimagit'
Plug 'vimwiki/vimwiki'
Plug 'tpope/vim-commentary'
Plug 'ap/vim-css-color'
" Plug 'reini-1/vim-code-darker'
Plug 'vim-scripts/AutoComplPop'
" Plug 'vimoxide/vim-cinnabar'
" Plug 'aonemd/kuroi.vim'
Plug 'lucasprag/simpleblack'
call plug#end()

" Use system clipboard

filetype plugin indent on

set clipboard+=unnamedplus

set wildmode=longest,list,full

" filetype plugin on

syntax enable

" Vertically center document when entering insert mode
autocmd InsertEnter * norm zz

" Color
colorscheme simpleblack
set termguicolors
set t_Co=256
set background=dark
" hi Normal guibg=NONE ctermbg=NONE
" autocmd vimenter * hi Normal guibg=NONE ctermbg=NONE " transparent bg

let g:lightline = {
      \ 'mode_map': {
        \ 'n' : 'N',
        \ 'i' : 'I',
        \ 'R' : 'R',
        \ 'v' : 'V',
        \ 'V' : 'VL',
        \ "\<C-v>": 'VB',
        \ 'c' : 'C',
        \ 's' : 'S',
        \ 'S' : 'SL',
        \ "\<C-s>": 'SB',
        \ 't': 'T',
        \ },
      \ }

" set mouse=a
set encoding=utf-8
set relativenumber
set nohlsearch
set noerrorbells
set laststatus=2
" Tabs
set shiftwidth=2
set softtabstop=2
set tabstop=2

set splitbelow splitright
set shiftwidth=4
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set splitright
set nobackup
set undofile
set incsearch
set scrolloff=8
set noshowmode
set completeopt=menuone,longest
set complete+=kspell
" set spell
" set nospell
set spelllang=en_us

" Shortcutting split navigation
map <A-h> <C-w>h
map <A-j> <C-w>j
map <A-k> <C-w>k
map <A-l> <C-w>l
map <A-<> <C-w>>
map <A->> <C-w><

nnoremap <leader>q :wq<CR>
nnoremap <leader>w :w<CR>
nnoremap <leader>g :Goyo<cr>
nnoremap <C-j>      gt
nnoremap <C-k>      gT
nnoremap <A-t>     :tabnew<CR>
nnoremap <A-q>     :close<CR>
nnoremap <A-tab>   :call ToggleNetrw()<cr>
nnoremap <A-o>     :find 


"command! MakeTags !ctags -R .

let g:netrw_banner=0        " disable annoying banner
"let g:netrw_browse_split=4  " open in prior window
let g:netrw_winsize = 15
let g:netrw_altv=1          " open splits to the right
let g:netrw_liststyle=3     " tree view
let g:netrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide.=',\(^\|\s\s\)\zs\.\S\+'

set path+=**

function! OpenToRight()
	:normal v
	let g:path=expand('%:p')
	execute 'q!'
	execute 'belowright vnew' g:path
	:normal <C-w>l
endfunction

function! OpenBelow()
	:normal v
	let g:path=expand('%:p')
	execute 'q!'
	execute 'belowright new' g:path
	:normal <C-w>l
endfunction

function! OpenTab()
	:normal v
	let g:path=expand('%:p')
	execute 'q!'
	execute 'tabedit' g:path
	:normal <C-w>l
endfunction

function! NetrwMappings()
		" Hack fix to make ctrl-l work properly
		noremap <buffer> <A-l> <C-w>l
		noremap <buffer> <C-l> <C-w>l
		noremap <silent> <A-f> :call ToggleNetrw()<CR>
		noremap <buffer> V :call OpenToRight()<cr>
		noremap <buffer> H :call OpenBelow()<cr>
		noremap <buffer> T :call OpenTab()<cr>
		noremap <buffer> <.> gh
endfunction

augroup netrw_mappings
		autocmd!
		autocmd filetype netrw call NetrwMappings()
augroup END

" Allow for netrw to be toggled
function! ToggleNetrw()
		if g:NetrwIsOpen
				let i = bufnr("$")
				while (i >= 1)
						if (getbufvar(i, "&filetype") == "netrw")
								silent exe "bwipeout " . i
						endif
						let i-=1
				endwhile
				let g:NetrwIsOpen=0
		else
				let g:NetrwIsOpen=1
				silent Lexplore
		endif
endfunction

" Check before opening buffer on any file
function! NetrwOnBufferOpen()
	if exists('b:noNetrw')
			return
	endif
	call ToggleNetrw()
endfun

" Close Netrw if it's the only buffer open
autocmd WinEnter * if winnr('$') == 1 && getbufvar(winbufnr(winnr()), "&filetype") == "netrw" || &buftype == 'quickfix' |q|endif

" Make netrw act like a project Draw
augroup ProjectDrawer
	autocmd!
	" Don't open Netrw
	" autocmd VimEnter ~/.config/joplin/tmp/*,/tmp/calcurse*,~/.calcurse/notes/*,~/vimwiki/*,*/.git/COMMIT_EDITMSG let b:noNetrw=1
	" autocmd VimEnter * :call NetrwOnBufferOpen()
augroup END

let g:NetrwIsOpen=0
