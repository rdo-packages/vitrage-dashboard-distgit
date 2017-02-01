%global pypi_name vitrage-dashboard
%global mod_name vitragedashboard

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-vitrage-ui
Version:        XXX
Release:        XXX
Summary:        Vitrage Management Dashboard

License:        ASL 2.0
URL:            https://github.com/openstack/vitrage-dashboard
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx

Requires: python-babel
Requires: openstack-dashboard
Requires: python-iso8601
Requires: python-keystoneclient
Requires: python-vitrageclient

%description
Vitrage Management Dashboard


%prep
%setup -q -n vitrage-dashboard-%{upstream_version}
# Remove bundled egg-info
rm {test-,}requirements.txt

%build
%{__python2} setup.py build


%install
%{__python2} setup.py install --skip-build --root %{buildroot}

# Move config to horizon
mkdir -p  %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled
mkdir -p  %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled

mv vitragedashboard/enabled/_80_project_vitrage_panel_group.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/_80_project_vitrage_panel_group.py
mv vitragedashboard/enabled/_90_project_topology_vitrage_panel.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/_90_project_topology_vitrage_panel.py
mv vitragedashboard/enabled/_91_project_alarms_vitrage_panel.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/_91_project_alarms_vitrage_panel.py
mv vitragedashboard/enabled/_92_project_entities_vitrage_panel.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/_92_project_entities_vitrage_panel.py
mv vitragedashboard/enabled/_93_project_template_vitrage_panel.py %{buildroot}%{_sysconfdir}/openstack-dashboard/enabled/_93_project_template_vitrage_panel.py

ln -s %{_sysconfdir}/openstack-dashboard/enabled/_80_project_vitrage_panel_group.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_80_project_vitrage_panel_group.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_90_project_topology_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_90_project_topology_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_91_project_alarms_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_91_project_alarms_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_92_project_entities_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_92_project_entities_vitrage_panel.py
ln -s %{_sysconfdir}/openstack-dashboard/enabled/_93_project_template_vitrage_panel.py %{buildroot}%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_93_project_template_vitrage_panel.py


%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{mod_name}
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/vitragealarms
%{python2_sitelib}/vitrageentities
%{python2_sitelib}/vitragetemplates

%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_80_project_vitrage_panel_group.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_90_project_topology_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_91_project_alarms_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_92_project_entities_vitrage_panel.py*
%{_datadir}/openstack-dashboard/openstack_dashboard/local/enabled/_93_project_template_vitrage_panel.py*

%{_sysconfdir}/openstack-dashboard/enabled/_80_project_vitrage_panel_group.py*
%{_sysconfdir}/openstack-dashboard/enabled/_90_project_topology_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_91_project_alarms_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_92_project_entities_vitrage_panel.py*
%{_sysconfdir}/openstack-dashboard/enabled/_93_project_template_vitrage_panel.py*


%changelog
