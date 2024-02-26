# COSMIC Desktop meta package
Name:           cosmic-applets
Version:        0.1.0~20240226

Release:        %autorelease
Summary:        WIP applets for the COSMIC Desktop Environment

License:        GPL-3.0

URL:            https://github.com/pop-os/cosmic-epoch

Requires:       cosmic-applet-app-list
Requires:       cosmic-applet-audio
Requires:       cosmic-applet-battery
Requires:       cosmic-applet-bluetooth
Requires:       cosmic-applet-network
Requires:       cosmic-applet-notifications
Requires:       cosmic-applet-panel-button
Requires:       cosmic-applet-power
Requires:       cosmic-applet-status-area
Requires:       cosmic-applet-tiling
Requires:       cosmic-applet-time
Requires:       cosmic-applet-workspaces


%global _description %{expand:
%{summary}.}

%description %{_description}

%prep

%build

%install

%files

%changelog
%autochangelog
    