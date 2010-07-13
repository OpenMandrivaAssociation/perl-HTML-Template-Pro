%define upstream_name    HTML-Template-Pro
%define upstream_version 0.9502

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Perl/XS module to use HTML Templates from CGI scripts
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRequires: pcre-devel
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)
BuildRequires: perl(JSON)
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Original HTML::Template is written by Sam Tregar, sam@tregar.com with
contributions of many people mentioned there. Their efforts caused
HTML::Template to be mature html tempate engine which separate perl code
and html design. Yet powerful, HTML::Template is slow, especially if
mod_perl isn't available or in case of disk usage and memory limitations.

HTML::Template::Pro is a fast lightweight C/Perl+XS reimplementation of
HTML::Template (as of 2.8) and HTML::Template::Expr (as of 0.0.5). It is
not intended to be a complete replacement, but to be a fast implementation
of HTML::Template if you don't need quering, the extended facility of
HTML::Template. Designed for heavy upload, resource limitations, abcence of
mod_perl.

HTML::Template::Pro has complete support of filters and
HTML::Template::Expr's tag EXPR="<expression>", including user-defined
functions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorarch/HTML
%perl_vendorarch/auto/HTML
