%define real_name	IO-Zlib
%define name		perl-%{real_name}
%define version		1.04
%define release		%mkrel 3

Summary:	IO:: style interface to Compress::Zlib
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root
URL:		http://search.cpan.org/dist/%{real_name}
Source:		http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{real_name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-Compress-Zlib

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%__make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/IO/*
%{_mandir}/man?/*


* Tue Jun 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.04-2mdk
- Rebuild

* Thu Oct 14 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.04-1mdk
- 1.04

* Mon Aug 23 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03

* Wed Jun 30 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.01-1mdk
- first version of rpm.
