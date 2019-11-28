%{?!dnf_lowest_compatible: %global dnf_lowest_compatible 4.2.14}
%define dnf_plugins_extra 2.0.0
%define hawkey_version 0.37.0

# Copr targets are not available for OpenMandriva
%bcond_with copr_plugin

Summary:	Core Plugins for DNF
Name:		dnf-plugins-core
Version:	4.0.12
Release:	1
Group:		System/Configuration/Packaging
License:	GPLv2+
URL:		https://github.com/rpm-software-management/%{name}
Source0:	https://github.com/rpm-software-management/dnf-plugins-core/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		dnf-plugins-core-4.0.4-sphinx-build.patch

BuildArch:	noarch
BuildRequires:	cmake
BuildRequires:	gettext
Requires:	python-dnf-plugins-core = %{version}-%{release}
Provides:	dnf-command(builddep)
Provides:	dnf-command(changelog)
Provides:	dnf-command(config-manager)
%if %{with copr_plugin}
Provides:	dnf-command(copr)
%endif
Provides:	dnf-command(debug-dump)
Provides:	dnf-command(debug-restore)
Provides:	dnf-command(debuginfo-install)
Provides:	dnf-command(download)
Provides:	dnf-command(repoclosure)
Provides:	dnf-command(repodiff)
Provides:	dnf-command(repograph)
Provides:	dnf-command(repomanage)
Provides:	dnf-command(reposync)

# Plugins shift from extras to core
Provides:	dnf-plugins-extras-debug = %{version}-%{release}
Provides:	dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:	dnf-plugins-extras-repograph = %{version}-%{release}
Provides:	dnf-plugins-extras-repomanage = %{version}-%{release}
# Generic package name Provides
Provides:	dnf-plugin-builddep = %{version}-%{release}
Provides:	dnf-plugin-config-manager = %{version}-%{release}
Provides:	dnf-plugin-debuginfo-install = %{version}-%{release}
Provides:	dnf-plugin-download = %{version}-%{release}
Provides:	dnf-plugin-generate_completion_cache = %{version}-%{release}
Provides:	dnf-plugin-needs_restarting = %{version}-%{release}
Provides:	dnf-plugin-repoclosure = %{version}-%{release}
Provides:	dnf-plugin-repodiff = %{version}-%{release}
Provides:	dnf-plugin-repograph = %{version}-%{release}
Provides:	dnf-plugin-repomanage = %{version}-%{release}
Provides:	dnf-plugin-reposync = %{version}-%{release}
Conflicts:	dnf-plugins-extras-common-data < %{dnf_plugins_extra}

%description
Core Plugins for DNF. This package enhances DNF with the builddep,
config-manager, %{?_with_copr_plugin:copr, }debug, debuginfo-install,
download, needs-restarting, repoclosure, repograph, repomanage,
and reposync commands. Additionally, it provides the
generate_completion_cache passive plugin.

%package -n python-dnf-plugins-core
Summary:	Python 3 interface to core plugins for DNF
Group:		System/Configuration/Packaging
BuildRequires:	pkgconfig(python)
BuildRequires:	python-dnf >= %{dnf_lowest_compatible}
BuildRequires:	python-nose
BuildRequires:	python-sphinx
BuildRequires:	python-setuptools
Requires:	python-dnf >= %{dnf_lowest_compatible}
Requires:	python-hawkey >= %{hawkey_version}
Requires:	python-dateutil
#Requires:	python3egg(distro)

Conflicts:	%{name} <= 0.1.5
# let the both python plugin versions be updated simultaneously
Conflicts:	python-%{name} < %{version}-%{release}
Conflicts:	python2-%{name} < %{version}-%{release}
Provides:	python-dnf-plugins-extras-debug = %{version}-%{release}
Provides:	python-dnf-plugins-extras-repoclosure = %{version}-%{release}
Provides:	python-dnf-plugins-extras-repograph = %{version}-%{release}
Provides:	python-dnf-plugins-extras-repomanage = %{version}-%{release}
Obsoletes:	python-dnf-plugins-extras-debug < %{dnf_plugins_extra}
Obsoletes:	python-dnf-plugins-extras-repoclosure < %{dnf_plugins_extra}
Obsoletes:	python-dnf-plugins-extras-repograph < %{dnf_plugins_extra}
Obsoletes:	python-dnf-plugins-extras-repomanage < %{dnf_plugins_extra}

%description -n python-dnf-plugins-core
Core Plugins for DNF, Python 3 interface. This package enhances DNF with
the builddep, config-manager, %{?_with_copr_plugin:copr, }debug,
debuginfo-install, download, needs-restarting, repoclosure, repograph,
repomanage, and reposync commands.

Additionally, it provides the generate_completion_cache passive plugin.

%package -n dnf-utils
Summary:	Yum-utils CLI compatibility layer
Group:		System/Configuration/Packaging
Conflicts:	yum-utils
# Allow GDB to have dnf-utils satisfy its requirement for debuginfo-install command
Provides:	pkg-command(debuginfo-install)
# Conflict with other provider of /usr/bin/debuginfo-install
Conflicts:	urpmi-debug-info-install
# Conflict with older versions where debuginfo-install was bundled
Conflicts:	gdb < 8.0
Requires:	dnf >= %{dnf_lowest_compatible}
Requires:	%{name} = %{version}-%{release}
Requires:	python-dnf >= %{dnf_lowest_compatible}

%description -n dnf-utils
As a Yum-utils CLI compatibility layer, supplies in CLI shims for
debuginfo-install, repograph, package-cleanup, repoclosure, repodiff, repomanage,
repoquery, reposync, repotrack, builddep, config-manager, debug, and
download that use new implementations using DNF.

%package -n python-dnf-plugin-leaves
Summary:	Leaves Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name} = %{version}-%{release}
Provides:	python-dnf-plugins-extras-leaves = %{version}-%{release}
Provides:	dnf-command(leaves)
Provides:	dnf-plugin-leaves = %{version}-%{release}
Provides:	dnf-plugins-extras-leaves = %{version}-%{release}
Conflicts:	dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:	python2-dnf-plugin-leaves < %{version}-%{release}
Obsoletes:	python-dnf-plugins-extras-leaves < %{dnf_plugins_extra}

%description -n python-dnf-plugin-leaves
Leaves Plugin for DNF, Python 3 version. List all installed packages
not required by any other installed package.

%package -n python-dnf-plugin-local
Summary:	Local Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	createrepo_c
Requires:	python-%{name} = %{version}-%{release}
Provides:	dnf-plugin-local =  %{version}-%{release}
Provides:	python-dnf-plugins-extras-local = %{version}-%{release}
Provides:	dnf-plugins-extras-local = %{version}-%{release}
Conflicts:	dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:	python2-dnf-plugin-local < %{version}-%{release}
Obsoletes:	python-dnf-plugins-extras-local < %{dnf_plugins_extra}

%description -n python-dnf-plugin-local
Local Plugin for DNF, Python 3 version. Automatically copy all downloaded
packages to a repository on the local filesystem and generating repo metadata.

%package -n python-dnf-plugin-show-leaves
Summary:	Show-leaves Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name} = %{version}-%{release}
Requires:	python-dnf-plugin-leaves = %{version}-%{release}
Provides:	dnf-plugin-show-leaves =  %{version}-%{release}
Provides:	python-dnf-plugins-extras-show-leaves = %{version}-%{release}
Provides:	dnf-command(show-leaves)
Provides:	dnf-plugins-extras-show-leaves = %{version}-%{release}
Conflicts:	dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:	python2-dnf-plugin-show-leaves < %{version}-%{release}
Obsoletes:	python-dnf-plugins-extras-show-leaves < %{dnf_plugins_extra}

%description -n python-dnf-plugin-show-leaves
Show-leaves Plugin for DNF, Python 3 version. List all installed
packages that are no longer required by any other installed package
after a transaction.

%package -n python-dnf-plugin-versionlock
Summary:	Version Lock Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name} = %{version}-%{release}
Provides:	dnf-plugin-versionlock =  %{version}-%{release}
Provides:	python-dnf-plugins-extras-versionlock = %{version}-%{release}
Provides:	dnf-command(versionlock)
Provides:	dnf-plugins-extras-versionlock = %{version}-%{release}
Conflicts:	dnf-plugins-extras-common-data < %{dnf_plugins_extra}
Conflicts:	python2-dnf-plugin-versionlock < %{version}-%{release}
Obsoletes:	python-dnf-plugins-extras-versionlock < %{dnf_plugins_extra}

%description -n python-dnf-plugin-versionlock
Version lock plugin takes a set of name/versions for packages
and excludes all other versions of those packages. This allows
you to e.g. protect packages from being updated by newer versions.

%prep
%autosetup -p1

%build
%cmake -DPYTHON_DESIRED:str=3
%make_build
make doc-man

%install
%make_install -C build

%find_lang %{name}

mv %{buildroot}%{_libexecdir}/dnf-utils-3 %{buildroot}%{_libexecdir}/dnf-utils

mkdir -p %{buildroot}%{_bindir}
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/debuginfo-install
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/needs-restarting
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/find-repos-of-install
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repo-graph
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/package-cleanup
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoclosure
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repodiff
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repomanage
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repoquery
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/reposync
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/repotrack
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-builddep
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-config-manager
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-dump
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yum-debug-restore
ln -sf %{_libexecdir}/dnf-utils %{buildroot}%{_bindir}/yumdownloader

# Purge man page for not installed migrate plugin
rm -f %{buildroot}%{_mandir}/man8/dnf-migrate.8*

# Ensure code is byte compiled
%py_compile %{buildroot}

%check
PYTHONPATH=./plugins /usr/bin/nosetests -s tests/

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.rst
%{_mandir}/man8/dnf-builddep.*
%{_mandir}/man8/dnf-config-manager.*
%if %{with copr_plugin}
%{_mandir}/man8/dnf-.copr.*
%else
%exclude %{_mandir}/man8/dnf-copr.*
%endif
%{_mandir}/man1/dnf-utils.*
%{_mandir}/man1/package-cleanup.*
%{_mandir}/man1/yumdownloader.*
%{_mandir}/man8/yum-copr.*
%{_mandir}/man1/yum-changelog.*
%{_mandir}/man1/debuginfo-install.*
%{_mandir}/man1/needs-restarting.*
%{_mandir}/man1/repo-graph.*
%{_mandir}/man1/repoclosure.*
%{_mandir}/man1/repodiff.*
%{_mandir}/man1/repomanage.*
%{_mandir}/man1/reposync.*
%{_mandir}/man1/yum-builddep.*
%{_mandir}/man1/yum-config-manager.*
%{_mandir}/man1/yum-debug-dump.*
%{_mandir}/man1/yum-debug-restore.*
%{_mandir}/man1/yum-utils.1.xz
%{_mandir}/man8/dnf-changelog.*
%{_mandir}/man8/dnf-debug.*
%{_mandir}/man8/dnf-debuginfo-install.*
%{_mandir}/man8/dnf-download.*
%{_mandir}/man8/dnf-generate_completion_cache.*
%{_mandir}/man1/dnf-needs-restarting.*
%{_mandir}/man8/dnf-repoclosure.*
%{_mandir}/man8/dnf-repodiff.*
%{_mandir}/man8/dnf-repograph.*
%{_mandir}/man8/dnf-repomanage.*
%{_mandir}/man8/dnf-reposync.*
%dir %{_sysconfdir}/dnf/protected.d
%ghost %{_var}/cache/dnf/packages.db
%config(noreplace) %{_sysconfdir}/dnf/plugins/debuginfo-install.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/copr.conf

%files -n python-dnf-plugins-core
%license COPYING
%doc AUTHORS README.rst
%{python3_sitelib}/dnf-plugins/builddep.py
%{python3_sitelib}/dnf-plugins/__pycache__/builddep.*
%{python3_sitelib}/dnf-plugins/config_manager.py
%{python3_sitelib}/dnf-plugins/__pycache__/config_manager.*
%if %{with copr_plugin}
%{python3_sitelib}/dnf-plugins/copr.py
%{python3_sitelib}/dnf-plugins/__pycache__/copr.*
%else
%exclude %{python3_sitelib}/dnf-plugins/copr.*
%exclude %{python3_sitelib}/dnf-plugins/__pycache__/copr.*
%endif
%{python3_sitelib}/dnf-plugins/changelog.py
%{python3_sitelib}/dnf-plugins/__pycache__/changelog.*
%{python3_sitelib}/dnf-plugins/debug.py
%{python3_sitelib}/dnf-plugins/__pycache__/debug.*
%{python3_sitelib}/dnf-plugins/debuginfo-install.py
%{python3_sitelib}/dnf-plugins/__pycache__/debuginfo-install.*
%{python3_sitelib}/dnf-plugins/download.py
%{python3_sitelib}/dnf-plugins/__pycache__/download.*
%{python3_sitelib}/dnf-plugins/generate_completion_cache.py
%{python3_sitelib}/dnf-plugins/__pycache__/generate_completion_cache.*
%{python3_sitelib}/dnf-plugins/needs_restarting.py
%{python3_sitelib}/dnf-plugins/__pycache__/needs_restarting.*
%{python3_sitelib}/dnf-plugins/repoclosure.py
%{python3_sitelib}/dnf-plugins/__pycache__/repoclosure.*
%{python3_sitelib}/dnf-plugins/repodiff.py
%{python3_sitelib}/dnf-plugins/__pycache__/repodiff.*
%{python3_sitelib}/dnf-plugins/repograph.py
%{python3_sitelib}/dnf-plugins/__pycache__/repograph.*
%{python3_sitelib}/dnf-plugins/repomanage.py
%{python3_sitelib}/dnf-plugins/__pycache__/repomanage.*
%{python3_sitelib}/dnf-plugins/reposync.py
%{python3_sitelib}/dnf-plugins/__pycache__/reposync.*
%{python3_sitelib}/dnfpluginscore/

%files -n dnf-utils
%{_libexecdir}/dnf-utils
%{_bindir}/debuginfo-install
%{_bindir}/needs-restarting
%{_bindir}/find-repos-of-install
%{_bindir}/package-cleanup
%{_bindir}/repo-graph
%{_bindir}/repoclosure
%{_bindir}/repodiff
%{_bindir}/repomanage
%{_bindir}/repoquery
%{_bindir}/reposync
%{_bindir}/repotrack
%{_bindir}/yum-builddep
%{_bindir}/yum-config-manager
%{_bindir}/yum-debug-dump
%{_bindir}/yum-debug-restore
%{_bindir}/yumdownloader

%files -n python-dnf-plugin-leaves
%{python3_sitelib}/dnf-plugins/leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/leaves.*
%{_mandir}/man8/dnf-leaves.*

%files -n python-dnf-plugin-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python3_sitelib}/dnf-plugins/local.*
%{python3_sitelib}/dnf-plugins/__pycache__/local.*
%{_mandir}/man8/dnf-local.*

%files -n python-dnf-plugin-show-leaves
%{python3_sitelib}/dnf-plugins/show_leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/show_leaves.*
%{_mandir}/man8/dnf-show-leaves.*

%files -n python-dnf-plugin-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python3_sitelib}/dnf-plugins/versionlock.*
%{python3_sitelib}/dnf-plugins/__pycache__/versionlock.*
%{_mandir}/man8/dnf-versionlock.*
%{_mandir}/man5/yum-versionlock.conf.5*
%{_mandir}/man8/yum-versionlock.8*
