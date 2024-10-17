%define upstream_name    HTML-Template-Pro
%define upstream_version 0.9510

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.9510
Release:	3

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Perl/XS module to use HTML Templates from CGI scripts
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/HTML-Template-Pro-0.9510.tar.gz

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


%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 0.950.500-3
+ Revision: 773023
- relink against libpcre.so.1

* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.950.500-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.950.500-1
+ Revision: 690265
- update to new version 0.9505

* Tue Aug 31 2010 Jérôme Quelin <jquelin@mandriva.org> 0.950.300-1mdv2011.0
+ Revision: 574787
- update to 0.9503

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.950.200-2mdv2011.0
+ Revision: 555954
- rebuild for perl 5.12

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.950.200-1mdv2011.0
+ Revision: 552317
- update to 0.9502

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-2mdv2010.1
+ Revision: 529780
- rebuild
- update to 0.94
- update to 0.94

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.1
+ Revision: 469439
- update to 0.93

* Wed Sep 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 451154
- update to 0.92

* Mon Sep 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1mdv2010.0
+ Revision: 439672
- update to new version 0.90

* Sun Aug 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.870.0-1mdv2010.0
+ Revision: 422560
- update to 0.87

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.0
+ Revision: 420893
- update to 0.86

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.850.0-1mdv2010.0
+ Revision: 415005
- update to 0.85

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.810.0-1mdv2010.0
+ Revision: 408835
- update to 0.81

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.800.0-1mdv2010.0
+ Revision: 399300
- update to 0.80
- using %%perl_convert_version
- fixed license field

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.76-1mdv2010.0
+ Revision: 396219
- update to new version 0.76

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2010.0
+ Revision: 392989
- update to new version 0.75

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.74-1mdv2010.0
+ Revision: 370129
- update to new version 0.74

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.72-1mdv2009.1
+ Revision: 320435
- update to new version 0.72

* Sun Sep 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-1mdv2009.0
+ Revision: 282127
- update to new version 0.71

* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.70-1mdv2009.0
+ Revision: 235621
- import perl-HTML-Template-Pro


* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.70-1mdv2009.0
- initial mdv release, generated with cpan2dist



