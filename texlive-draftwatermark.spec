# revision 25045
# category Package
# catalog-ctan /macros/latex/contrib/draftwatermark
# catalog-date 2007-03-05 22:02:45 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-draftwatermark
Version:	1.2
Release:	1
Summary:	Put a grey textual watermark on document pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/draftwatermark
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftwatermark.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftwatermark.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/draftwatermark.source.tar.xz
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
%{_texmfdistdir}/tex/latex/draftwatermark/draftwatermark.sty
%doc %{_texmfdistdir}/doc/latex/draftwatermark/README
%doc %{_texmfdistdir}/doc/latex/draftwatermark/draftwatermark.pdf
%doc %{_texmfdistdir}/doc/latex/draftwatermark/test_draftwatermark.tex
#- source
%doc %{_texmfdistdir}/source/latex/draftwatermark/draftwatermark.dtx
%doc %{_texmfdistdir}/source/latex/draftwatermark/draftwatermark.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-3
+ Revision: 758860
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 751087
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718259
- texlive-draftwatermark
- texlive-draftwatermark
- texlive-draftwatermark
- texlive-draftwatermark

