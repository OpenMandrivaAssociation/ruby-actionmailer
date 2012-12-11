%define	rname	actionmailer

Summary:	Service layer for easy email delivery and testing
Name:		ruby-%{rname}
Version:	3.2.3
Release:	1
URL:		http://www.rubyonrails.org/
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
rm -rf %{buildroot}
gem install --ri -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.2.3-1
+ Revision: 796014
- update to 3.2.3

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 3.2.1-1
+ Revision: 769662
- New release

* Tue Mar 15 2011 Rémy Clouard <shikamaru@mandriva.org> 2.3.11-2
+ Revision: 645161
- new version 2.3.11

* Thu Dec 09 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-2mdv2011.0
+ Revision: 618288
- add provides to fix rails dependencies

* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-1mdv2011.0
+ Revision: 585831
- bump release

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.9-1mdv2011.0
+ Revision: 579506
- new release: 2.3.9

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.4-1mdv2010.0
+ Revision: 438622
- Update to new version 2.3.4

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.3-1mdv2010.0
+ Revision: 404437
- Update to new version 2.3.3

* Fri Jun 12 2009 Lev Givon <lev@mandriva.org> 2.1.2-1mdv2010.0
+ Revision: 385325
- Update to 2.1.2.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-2mdv2009.0
+ Revision: 269226
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.1.0-1mdv2009.0
+ Revision: 214650
- new version 2.1.0

* Mon Jan 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 151355
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Olivier Blin <blino@mandriva.org> 1.3.3-1mdv2008.0
+ Revision: 17585
- 1.3.3

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 1.2.5-2mdv2008.0
+ Revision: 16673
- ri is now in ri/ and not ri/ri/
- Use Development/Ruby group


* Thu Nov 16 2006 Olivier Blin <oblin@mandriva.com> 1.2.5-1mdv2007.0
+ Revision: 84942
- 1.2.5
- Import ruby-actionmailer

* Sat Jul 29 2006 Olivier Blin <blino@mandriva.com> 1.2.3-1mdv2007.0
- 1.2.3
- don't version requires

* Thu Feb 16 2006 Pascal Terjan <pterjan@mandriva.org> 1.1.5-2mdk
- Fix Requires syntax

* Thu Feb 16 2006 Pascal Terjan <pterjan@mandriva.org> 1.1.5-1mdk
- First Mandriva release

