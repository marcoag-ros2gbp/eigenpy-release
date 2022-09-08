%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-eigenpy
Version:        2.7.13
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS eigenpy package

License:        BSD
URL:            https://github.com/stack-of-tasks/eigenpy
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       boost-python%{python3_pkgversion}-devel
Requires:       eigen3-devel
Requires:       python%{python3_pkgversion}-devel
Requires:       python%{python3_pkgversion}-numpy
Requires:       ros-rolling-ros-workspace
BuildRequires:  boost-devel
BuildRequires:  boost-python%{python3_pkgversion}-devel
BuildRequires:  cmake3
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  git
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Bindings between Numpy and Eigen using Boost.Python

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/rolling" \
    -DCMAKE_PREFIX_PATH="/opt/ros/rolling" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Thu Sep 08 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.13-1
- Autogenerated by Bloom

* Wed Aug 24 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.12-1
- Autogenerated by Bloom

* Sat Aug 13 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.11-1
- Autogenerated by Bloom

* Tue Aug 02 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.10-3
- Autogenerated by Bloom

* Tue Aug 02 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.10-2
- Autogenerated by Bloom

* Thu Jul 28 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.10-1
- Autogenerated by Bloom

* Sun Jul 24 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.8-1
- Autogenerated by Bloom

* Tue Jul 19 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.7-1
- Autogenerated by Bloom

* Mon Jul 18 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.6-2
- Autogenerated by Bloom

* Mon Jul 18 2022 Justin Carpentier <justin.carpentier@inria.fr> - 2.7.6-1
- Autogenerated by Bloom

