#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Big
Summary:	Math::Big - useful routines and packages with Math::BigInt/BigFloat
Summary(pl):	Math::Big - przydatne funkcje i pakiety oparte o Math::BigInt/BigFloat
Name:		perl-Math-Big
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	44f46494949198def1e391f604a6d341
BuildRequires:	perl-Math-BigInt >= 1.61
BuildRequires:	perl(Math::BigFloat) >= 1.36
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.61
Requires:	perl(Math::BigFloat) >= 1.36
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Big module contains some routines that may come in handy when
you want to do some math with really, really big (or small) numbers.

%description -l pl
Modu³ Math::Big zawiera trochê procedur, które mog± okazaæ siê pomocne
przy obróbce bardzo, bardzo du¿ych (lub ma³ych) liczb.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BENCHMARK BUGS CHANGES CREDITS LICENSE NEW README TODO
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*.txt
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
