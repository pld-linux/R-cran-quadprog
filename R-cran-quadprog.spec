%define		fversion	%(echo %{version} |tr r -)
%define		modulename	quadprog
Summary:	Functions to solve Quadratic Programming Problems
Summary(pl.UTF-8):	Funkcje do rozwiązywania problemów programowania kwadratowego
Name:		R-cran-%{modulename}
Version:	1.5r5
Release:	3
License:	GPL v2+
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	8442f37afd8d0b19b12e77d63e6515ad
BuildRequires:	R >= 2.8.1
BuildRequires:	blas-devel
BuildRequires:	gcc-fortran
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains routines and documentation for solving quadratic
programming problems.

%description -l pl.UTF-8
Pakiet zawiera biblioteki i dokumentację do rozwiązywania problemów
programowania kwadratowego.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%post
(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
 R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)

%postun
if [ -f %{_libdir}/R/bin/Rcmd ];then
	(cd %{_libdir}/R/library; umask 022; cat */CONTENTS > ../doc/html/search/index.txt
	R_HOME=%{_libdir}/R ../bin/Rcmd perl ../share/perl/build-help.pl --index)
fi

%files
%defattr(644,root,root,755)
%doc %{modulename}/{DESCRIPTION,ChangeLog,README}
%{_libdir}/R/library/%{modulename}
