%{?!dnf_lowest_compatible: %global dnf_lowest_compatible 1.1.9}
%{?!dnf_not_compatible: %global dnf_not_compatible 2.0}
%global hawkey_version 0.6.3

# There is no Python 3 version of DNF API
%bcond_with python3

# The copr plugin is not useful for OpenMandriva
%bcond_with copr_plugin

# Fedora package release versions are committed as versions in upstream
%define origrel 1

Name:       dnf-plugins-core
Version:    0.1.21
Release:    1
Summary:    Core Plugins for DNF
Group:      System/Configuration/Packaging
License:    GPLv2+
URL:        https://github.com/rpm-software-management/dnf-plugins-core
Source0:    https://github.com/rpm-software-management/%{name}/archive/%{name}-%{version}-%{origrel}.tar.gz

# From upstream
Patch0001:  0001-cls.chroot_config-inside-_guess_chroot-returns-None-.patch
Patch0002:  0001-builddep-install-requirements-by-provides-RhBug-1332.patch
Patch0003:  0002-builddep-install-by-files-as-well.patch
Patch0004:  0003-builddep-show-message-if-package-is-already-installe.patch
Patch0005:  0004-tests-remove-builddep-test.patch
Patch0006:  0005-builddep-always-try-to-install-by-provides.patch

# OpenMandriva specific patches
Patch1001:  1001-CMake-Fix-detection-of-Python-2.patch

BuildArch:  noarch

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  python-sphinx

%if %{with python3}
Requires:   python3-dnf-plugins-core = %{version}-%{release}
%else
Requires:   python2-dnf-plugins-core = %{version}-%{release}
%endif
Provides:   dnf-command(builddep)
Provides:   dnf-command(config-manager)
%if %{with copr_plugin}
Provides:   dnf-command(copr)
%endif
Provides:   dnf-command(debuginfo-install)
Provides:   dnf-command(download)
Provides:   dnf-command(repoquery)
Provides:   dnf-command(reposync)

%description
Core Plugins for DNF. This package enhances DNF with the builddep,
config-manager, %{?_with_copr_plugin:copr, }debuginfo-install, download,
needs-restarting, repoquery and reposync commands. Additionally, it provides
the generate_completion_cache, noroot and protected_packages passive plugins.

%package -n python2-dnf-plugins-core
Summary:    Python 2 interface to core plugins for DNF
Group:      System/Configuration/Packaging
BuildRequires:  python2-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python2-dnf < %{dnf_not_compatible}
BuildRequires:  python2-nose
BuildRequires:  python2-devel
Requires:   python2-dnf >= %{dnf_lowest_compatible}
Requires:   python2-dnf < %{dnf_not_compatible}
Requires:   python2-hawkey >= %{hawkey_version}
%description -n python2-dnf-plugins-core
Core Plugins for DNF, Python 2 interface. This package enhances DNF with the
builddep, %{?_with_copr_plugin:copr, }config-manager, debuginfo-install,
download, needs-restarting, repoquery and reposync commands. Additionally,
it provides the generate_completion_cache, noroot and protected_packages
passive
plugins.

%if %{with python3}
%package -n python-dnf-plugins-core
Summary:    Python 3 interface to core plugins for DNF
Group:      System/Configuration/Packaging
BuildRequires:  python-devel
BuildRequires:  python-dnf >= %{dnf_lowest_compatible}
BuildRequires:  python-dnf < %{dnf_not_compatible}
BuildRequires:  python-nose
Requires:   python-dnf >= %{dnf_lowest_compatible}
Requires:   python-dnf < %{dnf_not_compatible}
Requires:   python-hawkey >= %{hawkey_version}
%description -n python-dnf-plugins-core
Core Plugins for DNF, Python 3 interface. This package enhances DNF with
the builddep, %{?_with_copr_plugin:copr, }config-manager, debuginfo-install,
download, needs-restarting, repoquery and reposync commands. Additionally
it provides the generate_completion_cache, noroot and protected_packages
passive plugins.
%endif

%prep
%setup -q -n %{name}-%{name}-%{version}-%{origrel}
%apply_patches

%if %{with python3}
rm -rf py3
mkdir py3
%endif

# Drop the changelog section to keep sphinx from choking
sed -e '152,$ d' -i %{name}.spec

%build
%cmake -DPYTHON_DESIRED:str=2
%make
make doc-man

%if %{with python3}
pushd ../py3
%cmake -DPYTHON_DESIRED:str=3 ../../
%make
make doc-man
popd
%endif

%install
pushd ./build
%make_install
popd
%find_lang %{name}

%if %{with python3}
pushd ./py3/build
%make_install
popd
%endif

%if %{without copr_plugin}
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.copr*
rm -rf %{buildroot}%{python2_sitelib}/dnf-plugins/copr.*
%if %{with python3}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/copr.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/copr.*
%endif
%endif

%check
PYTHONPATH=./plugins /usr/bin/nosetests-2.* -s tests/
%if %{with python3}
PYTHONPATH=./plugins /usr/bin/nosetests-3.* -s tests/
%endif

%files -f %{name}.lang
%doc COPYING AUTHORS README.rst
%{_mandir}/man8/dnf.plugin.*
%dir %{_sysconfdir}/dnf/protected.d
%ghost %{_var}/cache/dnf/packages.db
%config(noreplace) %{_sysconfdir}/dnf/plugins/*

%files -n python2-dnf-plugins-core
%doc COPYING AUTHORS README.rst
%{python2_sitelib}/dnf-plugins/*
%{python2_sitelib}/dnfpluginscore/

%if %{with python3}
%files -n python-dnf-plugins-core
%doc COPYING AUTHORS README.rst
%{python3_sitelib}/dnf-plugins/*
%{python3_sitelib}/dnfpluginscore/
%endif
