# TODO:
# - convert to "-installer" type package?

# NOTE:
# Do not remove NoSource tags. Make sure DistFiles won't fetch Greenhopper sources.
#
# Todd Revolt from Atlassian told that:
#   * We are free to integrate Atlassian products into PLD. So we can write
#     installer scripts, create nosrc packages etc.
#   * We are not permitted to redistribute their products. That mean during
#     installation each user has to download Greenhopper from Atlassian web page.
#
# See Atlassian_EULA_3.0.pdf for more details.

%if 0
# Download sources manually:
wget -c http://downloads.atlassian.com/software/greenhopper/downloads/jira-greenhopper-plugin-4.4.1.jar
wget -c http://www.atlassian.com/about/licensing/Atlassian_EULA_3.0.pdf
%endif

%include	/usr/lib/rpm/macros.java

Summary:	Agile project management plugin for JIRA
Name:		jira-plugin-greenhopper
Version:	4.4.1
Release:	0.1
License:	Proprietary, not distributable
Group:		Libraries/Java
Source0:	jira-greenhopper-plugin-4.4.1.jar
# NoSource0-md5:	042297a4412d2ee4266f56e6a81e6dbf
NoSource:	0
Source1:	Atlassian_EULA_3.0.pdf
# NoSource1-md5:	9e87088024e3c5ee2e63a72a3e99a6cb
NoSource:	1
URL:		http://www.atlassian.com/software/greenhopper
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jira >= 4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Agile project management plugin for JIRA. GreenHopper is the perfect tool for
managing your backlog, planning sprints and tracking your team through the
entire release process.

%prep
%setup -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

%install
install -d $RPM_BUILD_ROOT%{_datadir}/jira/WEB-INF/lib
cp jira-greenhopper-plugin-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/jira/WEB-INF/lib/jira-greenhopper-plugin-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Atlassian_EULA_3.0.pdf
%{_datadir}/jira/WEB-INF/lib/jira-greenhopper-plugin-%{version}.jar
