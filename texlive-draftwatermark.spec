Name:		texlive-draftwatermark
Version:	70401
Release:	1
Summary:	Put a grey textual watermark on document pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/draftwatermark
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftwatermark.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftwatermark.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftwatermark.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a means to add a textual, light grey
watermark on every page or on the first page of a document.
Typical usage may consist in writing words such as DRAFT or
CONFIDENTIAL across document pages. The package performs a
similar function to that of draftcopy, but its implementation
is output device independent, and very made simple by relying
on everpage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/draftwatermark
%doc %{_texmfdistdir}/doc/latex/draftwatermark
#- source
%doc %{_texmfdistdir}/source/latex/draftwatermark

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
