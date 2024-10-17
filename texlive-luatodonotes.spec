Name:		texlive-luatodonotes
Version:	53825
Release:	2
Summary:	Add editing annotations in a LuaLaTeX document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/luatodonotes
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatodonotes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatodonotes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luatodonotes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to insert comments into a document
that suggest (for example) further editing that may be needed.
The comments are shown in the margins alongside the text;
different styles for the comments may be used; the styles are
selected using package options. The package is based on the
package todonotes, and depends heavily on Lua, so it can only
be used with LuaLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/lualatex/luatodonotes
%{_texmfdistdir}/tex/lualatex/luatodonotes
%doc %{_texmfdistdir}/doc/lualatex/luatodonotes

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
