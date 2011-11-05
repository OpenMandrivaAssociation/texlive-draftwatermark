# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/draftwatermark
# catalog-date 2007-03-05 22:02:45 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-draftwatermark
Version:	1.0
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides a means to add a textual, light grey
watermark on every page or on the first page of a document.
Typical usage may consist in writing words such as DRAFT or
CONFIDENTIAL across document pages. The package performs a
similar function to that of draftcopy, but its implementation
is output device independent, and very made simple by relying
on everpage.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/draftwatermark/draftwatermark.sty
%doc %{_texmfdistdir}/doc/latex/draftwatermark/README
%doc %{_texmfdistdir}/doc/latex/draftwatermark/draftwatermark.pdf
#- source
%doc %{_texmfdistdir}/source/latex/draftwatermark/draftwatermark.dtx
%doc %{_texmfdistdir}/source/latex/draftwatermark/draftwatermark.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
