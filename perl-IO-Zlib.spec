%define	module	IO-Zlib
%define	modver	1.10

Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	8

Summary:	IO:: style interface to Compress::Zlib
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/IO/%{module}-%{modver}.tar.gz

BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%prep
%setup -q -n %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/IO/*
%{_mandir}/man?/*

%changelog
* Thu Dec 20 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.100.0-7
- rebuild for new perl-5.16.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-5mdv2012.0
+ Revision: 765377
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-4
+ Revision: 763894
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-3
+ Revision: 667213
- mass rebuild

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-2mdv2010.1
+ Revision: 420979
- rebuild

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 396302
- update to 1.10
- using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.09-2mdv2009.0
+ Revision: 223802
- rebuild

* Tue Jan 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2008.1
+ Revision: 152933
- update to new version 1.09
- update to new version 1.09

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdv2008.1
+ Revision: 110286
- new version

* Sun Aug 05 2007 Funda Wang <fwang@mandriva.org> 1.07-1mdv2008.0
+ Revision: 59070
- New version 1.07


* Sun Jul 16 2006 Olivier Thauvin <nanardon@mandriva.org> 1.04-3mdv2007.0
+ Revision: 41253
- rebuild
- add %%check section
- Import perl-IO-Zlib

* Wed Jun 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.04-2mdk
- Rebuild

* Fri Oct 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.04-1mdk
- 1.04

* Tue Aug 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03

* Thu Jul 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.01-1mdk
- first version of rpm.

