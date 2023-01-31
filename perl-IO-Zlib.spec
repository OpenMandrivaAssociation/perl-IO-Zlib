%define	module	IO-Zlib

Summary:	IO:: style interface to Compress::Zlib
Name:		perl-%{module}
Version:	1.14
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/IO/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build OPTIMIZE="%{optflags}"

%check
make test

%install
%make_install

%files
%doc ChangeLog
%{perl_vendorlib}/IO/*
%{_mandir}/man3/*
