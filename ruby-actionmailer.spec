%define	rname	actionmailer

Summary:	Service layer for easy email delivery and testing
Name:		ruby-%{rname}
Version:	4.1.1
Release:	2
URL:		https://www.rubyonrails.org/
Source0:	http://rubygems.org/downloads/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 
Provides:	rubygem(%{rname})

%description
Makes it trivial to test and deliver emails sent from a single service layer.

%prep

%build

%install
gem install --ri -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec


