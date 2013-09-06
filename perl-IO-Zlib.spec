%define	module	IO-Zlib
%define	modver	1.10

Summary:	IO:: style interface to Compress::Zlib
Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	8
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/IO/%{module}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl-devel

%description
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence
to gzip/zlib compressed files. It provides many of the same methods as
the IO::Handle interface.

%prep
%setup -qn %{module}-%{modver}

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
%{_mandir}/man3/*

