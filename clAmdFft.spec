Summary:	AMD Accelerated Parallel Processing FFT Library
Summary(pl.UTF-8):	Akcelerowana, zrównoleglona wersja biblioteki FFT firmy AMD
Name:		clAmdFft
Version:	1.8.291
Release:	1
License:	AMD EULA
Group:		Libraries
# download using form at URL
Source0:	%{name}%{version}.tar.gz
# NoSource0-md5:	ccf0d2972adeb09ee1619225a63f413e
NoSource:	0
URL:		http://developer.amd.com/tools/heterogeneous-computing/amd-accelerated-parallel-processing-math-libraries/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no sources and library is missing -lpthread -ldl
%define		skip_post_check_so	libclAmdFft.Runtime.*

%description
AMD Accelerated Parallel Processing Math Libraries are software
libraries containing FFT and BLAS functions written in OpenCL and
designed to run on AMD GPUs. The libraries support running on CPU
devices to facilitate debugging and multicore programming.

This package contains FFT library.

%description -l pl.UTF-8
AMD APPML (Accelerated Parallel Processing Math Libraries -
akcelerowane, zrównoleglone biblioteki matematyczne) to biblioteki
programowe zawierające funkcje FFT i BLAS napisane z użyciem OpenCL i
zaprojektowane do uruchamiania na procesorach graficznych (GPU) firmy
AMD. Biblioteki obsługują uruchamianie na CPU w celu ułatwienia
diagnostyki i programowania wielordzeniowego.

Ten pakiet zawiera bibliotekę FFT.

%package devel
Summary:	Header files for OpenCL AMD FFT library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenCL AMD FFT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenCL-devel

%description devel
Header files for OpenCL AMD FFT library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenCL AMD FFT.

%prep
%setup -q -c

tar xf %{name}-%{version}-Linux.tar.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -p include/*.h $RPM_BUILD_ROOT%{_includedir}

%ifarch %{ix86}
cp -dp lib32/lib*.so* $RPM_BUILD_ROOT%{_libdir}
%endif

%ifarch %{x8664}
cp -dp lib64/lib*.so* $RPM_BUILD_ROOT%{_libdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc clAmdFft-{EULA,README}.txt
%attr(755,root,root) %{_libdir}/libclAmdFft.Runtime.so.*.*.*
%attr(755,root,root) %{_libdir}/libclAmdFft.StatTimer.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/clAmdFft.refman.pdf
%attr(755,root,root) %{_libdir}/libclAmdFft.Runtime.so
%attr(755,root,root) %{_libdir}/libclAmdFft.StatTimer.so
%{_includedir}/clAmdFft*.h
