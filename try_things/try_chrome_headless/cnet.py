#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Sigai"
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from html import unescape
import json

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.binary_location = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
opener = webdriver.Chrome(chrome_options=chrome_options)
urls = ["http://download.cnet.com/security/windows/", "http://download.cnet.com/security/windows/",
        "http://download.cnet.com/security-antivirus/windows/", "http://download.cnet.com/security-corporate/windows/",
        "http://download.cnet.com/security-encryption/windows/", "http://download.cnet.com/security-firewall/windows/",
        "http://download.cnet.com/security-internet-suites/windows/",
        "http://download.cnet.com/security-monitoring/windows/",
        "http://download.cnet.com/security-parental-control/windows/",
        "http://download.cnet.com/security-adblocker/windows/", "http://download.cnet.com/security-privacy/windows/",
        "http://download.cnet.com/security-antispyware/windows/", "http://download.cnet.com/security/windows/",
        "http://download.cnet.com/browsers/windows/", "http://download.cnet.com/browsers-chrome-extensions/windows/",
        "http://download.cnet.com/browsers-firefox-addons/windows/",
        "http://download.cnet.com/browsers-internet-explorer-plugins/windows/",
        "http://download.cnet.com/browsers-newsreaders/windows/", "http://download.cnet.com/browsers-offline/windows/",
        "http://download.cnet.com/browsers-plugins/windows/", "http://download.cnet.com/browsers-web/windows/",
        "http://download.cnet.com/browsers/windows/", "http://download.cnet.com/biz-soft/windows/",
        "http://download.cnet.com/business-finance/windows/", "http://download.cnet.com/business-applications/windows/",
        "http://download.cnet.com/business-crm/windows/", "http://download.cnet.com/business-databases/windows/",
        "http://download.cnet.com/business-document-manager/windows/",
        "http://download.cnet.com/business-ecommerce/windows/", "http://download.cnet.com/business-inventory/windows/",
        "http://download.cnet.com/business-office-suites/windows/",
        "http://download.cnet.com/business-presentation-tools/windows/",
        "http://download.cnet.com/business-project-managment/windows/",
        "http://download.cnet.com/business-resume-builder/windows/",
        "http://download.cnet.com/business-seo-sem-tools/windows/",
        "http://download.cnet.com/business-small-business-tools/windows/",
        "http://download.cnet.com/business-spreadsheets/windows/",
        "http://download.cnet.com/business-taxes-accounting/windows/",
        "http://download.cnet.com/business-voice-recognition/windows/",
        "http://download.cnet.com/business-word-processing/windows/", "http://download.cnet.com/biz-soft/windows/",
        "http://download.cnet.com/chat-voip-email/windows/", "http://download.cnet.com/chat-voip-email-chat/windows/",
        "http://download.cnet.com/chat-voip-email-dialup-connectivity/windows/",
        "http://download.cnet.com/chat-voip-email-clients/windows/",
        "http://download.cnet.com/chat-voip-email-utilities/windows/",
        "http://download.cnet.com/chat-voip-email-sms/windows/",
        "http://download.cnet.com/chat-voip-email-spam-filters/windows/",
        "http://download.cnet.com/chat-voip-email-net-phones/windows/",
        "http://download.cnet.com/chat-voip-email-webcam-video/windows/",
        "http://download.cnet.com/desktop-enhancements/windows/",
        "http://download.cnet.com/desktop-alarms-clocks/windows/",
        "http://download.cnet.com/desktop-clipboard/windows/", "http://download.cnet.com/desktop-cursors/windows/",
        "http://download.cnet.com/desktop-shell-desktop-management/windows/",
        "http://download.cnet.com/desktop-widgets-gadgets/windows/",
        "http://download.cnet.com/desktop-icon-tools/windows/", "http://download.cnet.com/desktop-icons/windows/",
        "http://download.cnet.com/desktop-launchers-shutdown/windows/",
        "http://download.cnet.com/desktop-tweaks/windows/",
        "http://download.cnet.com/desktop-virtual-managers/windows/", "http://download.cnet.com/developers/windows/",
        "http://download.cnet.com/developers-net/windows/", "http://download.cnet.com/developers-activex/windows/",
        "http://download.cnet.com/developers-editors/windows/",
        "http://download.cnet.com/developers-components-library/windows/",
        "http://download.cnet.com/developers-database/windows/",
        "http://download.cnet.com/developers-debugging/windows/",
        "http://download.cnet.com/developers-reference-tutorials/windows/",
        "http://download.cnet.com/developers-ides-coding/windows/",
        "http://download.cnet.com/developers-compliers-interpreters/windows/",
        "http://download.cnet.com/developers-java/windows/", "http://download.cnet.com/developers-tools-ides/windows/",
        "http://download.cnet.com/developers-management-distribution/windows/",
        "http://download.cnet.com/developers-source-code/windows/",
        "http://download.cnet.com/developers-specialized-tools/windows/",
        "http://download.cnet.com/developers-web-engineeering/windows/",
        "http://download.cnet.com/developers-web-design/windows/", "http://download.cnet.com/developers-xml/windows/",
        "http://download.cnet.com/digitalphoto/windows/",
        "http://download.cnet.com/digitalphoto-camera-firmware/windows/",
        "http://download.cnet.com/digitalphoto-tools/windows/",
        "http://download.cnet.com/digitalphoto-editing-processing/windows/",
        "http://download.cnet.com/digitalphoto-image-viewers/windows/",
        "http://download.cnet.com/digitalphoto-media-management/windows/",
        "http://download.cnet.com/digitalphoto-photo-sharing-publishing/windows/",
        "http://download.cnet.com/drivers/windows/", "http://download.cnet.com/drivers-sound-multimedia/windows/",
        "http://download.cnet.com/drivers-camera/windows/", "http://download.cnet.com/drivers-cd-dvd-drive/windows/",
        "http://download.cnet.com/drivers-game-controllers/windows/",
        "http://download.cnet.com/drivers-input-devices/windows/",
        "http://download.cnet.com/drivers-fax-modems-isdn/windows/",
        "http://download.cnet.com/drivers-bios-sysupdates/windows/", "http://download.cnet.com/drivers-mouse/windows/",
        "http://download.cnet.com/drivers-network/windows/", "http://download.cnet.com/drivers-printers/windows/",
        "http://download.cnet.com/drivers-scanners/windows/", "http://download.cnet.com/drivers-scsi/windows/",
        "http://download.cnet.com/drivers-storage-sys/windows/", "http://download.cnet.com/drivers-usb/windows/",
        "http://download.cnet.com/drivers-display-video/windows/", "http://download.cnet.com/education/windows/",
        "http://download.cnet.com/education-ebooks/windows/",
        "http://download.cnet.com/education-ebooks-reader-manager/windows/",
        "http://download.cnet.com/education-fine-arts/windows/",
        "http://download.cnet.com/education-genealogy/windows/",
        "http://download.cnet.com/education-health-nutrition/windows/",
        "http://download.cnet.com/education-language/windows/", "http://download.cnet.com/education-mapping/windows/",
        "http://download.cnet.com/education-mathematics/windows/", "http://download.cnet.com/education-other/windows/",
        "http://download.cnet.com/education-reference/windows/",
        "http://download.cnet.com/education-religion-spirituality/windows/",
        "http://download.cnet.com/education-science/windows/",
        "http://download.cnet.com/education-student-tools/windows/",
        "http://download.cnet.com/education-teaching-tools/windows/", "http://download.cnet.com/entertainment/windows/",
        "http://download.cnet.com/entertainment-astrology/windows/",
        "http://download.cnet.com/entertainment-software/windows/",
        "http://download.cnet.com/entertainment-humor/windows/",
        "http://download.cnet.com/entertainment-lifestyle/windows/",
        "http://download.cnet.com/entertainment-music/windows/",
        "http://download.cnet.com/entertainment-sports/windows/",
        "http://download.cnet.com/entertainment-tv-movies/windows/", "http://download.cnet.com/games/windows/",
        "http://download.cnet.com/games-action/windows/", "http://download.cnet.com/games-adventure/windows/",
        "http://download.cnet.com/games-casual/windows/", "http://download.cnet.com/games-board-tabletop/windows/",
        "http://download.cnet.com/games-casino-card/windows/", "http://download.cnet.com/games-driving-racing/windows/",
        "http://download.cnet.com/games-fps/windows/", "http://download.cnet.com/games-tools-editors-mods/windows/",
        "http://download.cnet.com/games-kids/windows/", "http://download.cnet.com/games-mmorpg/windows/",
        "http://download.cnet.com/games-other/windows/", "http://download.cnet.com/games-sudoku-crossword/windows/",
        "http://download.cnet.com/games-platformer/windows/", "http://download.cnet.com/games-rts/windows/",
        "http://download.cnet.com/games-rpg/windows/", "http://download.cnet.com/games-simulation/windows/",
        "http://download.cnet.com/games-sports/windows/", "http://download.cnet.com/games-strategy-war/windows/",
        "http://download.cnet.com/design/windows/", "http://download.cnet.com/design-modeling-3d/windows/",
        "http://download.cnet.com/design-animation/windows/", "http://download.cnet.com/design-cad/windows/",
        "http://download.cnet.com/design-desktop-publishing/windows/", "http://download.cnet.com/design-flash/windows/",
        "http://download.cnet.com/design-font-tools/windows/", "http://download.cnet.com/design-fonts/windows/",
        "http://download.cnet.com/design-illustration/windows/", "http://download.cnet.com/design-pdf/windows/",
        "http://download.cnet.com/design-photoshop/windows/", "http://download.cnet.com/home/windows/",
        "http://download.cnet.com/home-diy-howto/windows/", "http://download.cnet.com/home-hobbies/windows/",
        "http://download.cnet.com/home-inventory/windows/", "http://download.cnet.com/home-kids-parenting/windows/",
        "http://download.cnet.com/home-landscape-design/windows/", "http://download.cnet.com/home-misc/windows/",
        "http://download.cnet.com/home-food-cooking/windows/", "http://download.cnet.com/home-weather/windows/",
        "http://download.cnet.com/internet/windows/", "http://download.cnet.com/internet-blogging/windows/",
        "http://download.cnet.com/internet-bookmark-managers/windows/",
        "http://download.cnet.com/internet-dl-managers/windows/", "http://download.cnet.com/internet-ftp/windows/",
        "http://download.cnet.com/internet-misc/windows/", "http://download.cnet.com/internet-online-forms/windows/",
        "http://download.cnet.com/internet-online-storage-data-backup/windows/",
        "http://download.cnet.com/internet-file-sharing/windows/",
        "http://download.cnet.com/security-password-managers/windows/",
        "http://download.cnet.com/internet-search/windows/",
        "http://download.cnet.com/internet-social-networking/windows/", "http://download.cnet.com/itunes/windows/",
        "http://download.cnet.com/ios-backup-recovery/windows/", "http://download.cnet.com/ios-utilities/windows/",
        "http://download.cnet.com/ios-video-converter-transfer/windows/",
        "http://download.cnet.com/ios-artwork/windows/", "http://download.cnet.com/ios-controllers/windows/",
        "http://download.cnet.com/ios-streaming-sharing/windows/", "http://download.cnet.com/ios-itunes-tools/windows/",
        "http://download.cnet.com/ios-other/windows/", "http://download.cnet.com/audio/windows/",
        "http://download.cnet.com/audio-plugins-utilities/windows/", "http://download.cnet.com/audio-others/windows/",
        "http://download.cnet.com/audio-cd-dvd-burner/windows/", "http://download.cnet.com/audio-dj-software/windows/",
        "http://download.cnet.com/audio-karaoke/windows/", "http://download.cnet.com/audio-media-players/windows/",
        "http://download.cnet.com/audio-music-management/windows/",
        "http://download.cnet.com/audio-podcasting/windows/", "http://download.cnet.com/audio-ringtone/windows/",
        "http://download.cnet.com/audio-rippers-encorders/windows/",
        "http://download.cnet.com/audio-streaming-software/windows/", "http://download.cnet.com/networking/windows/",
        "http://download.cnet.com/networking-file-server/windows/",
        "http://download.cnet.com/networking-internet-ops/windows/",
        "http://download.cnet.com/networking-network-management/windows/",
        "http://download.cnet.com/networking-network-tools/windows/",
        "http://download.cnet.com/networking-print-server/windows/",
        "http://download.cnet.com/networking-remote-access/windows/",
        "http://download.cnet.com/networking-wireless/windows/", "http://download.cnet.com/productivity/windows/",
        "http://download.cnet.com/productivity-brainstorming-mindmapping/windows/",
        "http://download.cnet.com/productivity-calculators/windows/",
        "http://download.cnet.com/productivity-calenders-planners/windows/",
        "http://download.cnet.com/productivity-personal-info-managers/windows/",
        "http://download.cnet.com/productivity-other/windows/",
        "http://download.cnet.com/productivity-personal-finance/windows/",
        "http://download.cnet.com/productivity-notepad-apps/windows/",
        "http://download.cnet.com/customization/windows/",
        "http://download.cnet.com/customization-startup-shutdown/windows/",
        "http://download.cnet.com/customization-screensaver-tools/windows/",
        "http://download.cnet.com/customization-screensavers/windows/",
        "http://download.cnet.com/customization-skins/windows/",
        "http://download.cnet.com/customization-theme-editors/windows/",
        "http://download.cnet.com/customization-themes/windows/",
        "http://download.cnet.com/customization-wallpapers/windows/",
        "http://download.cnet.com/customization-wallpapers-tools/windows/", "http://download.cnet.com/travel/windows/",
        "http://download.cnet.com/travel-city-guides/windows/", "http://download.cnet.com/travel-currency/windows/",
        "http://download.cnet.com/travel-gps/windows/", "http://download.cnet.com/travel-planning-booking/windows/",
        "http://download.cnet.com/travel-language-translators/windows/",
        "http://download.cnet.com/travel-lists/windows/", "http://download.cnet.com/travel-maps/windows/",
        "http://download.cnet.com/travel-restaurants/windows/",
        "http://download.cnet.com/travel-transportation/windows/", "http://download.cnet.com/utilities/windows/",
        "http://download.cnet.com/utilities-widgets-plugins/windows/",
        "http://download.cnet.com/utilities-automation/windows/", "http://download.cnet.com/utilities-backup/windows/",
        "http://download.cnet.com/utilities-power-management/windows/",
        "http://download.cnet.com/utilities-calculators/windows/",
        "http://download.cnet.com/utilities-datatransfer-sync/windows/",
        "http://download.cnet.com/utilities-diagnostic/windows/",
        "http://download.cnet.com/utilities-file-compression/windows/",
        "http://download.cnet.com/utilities-file-management/windows/",
        "http://download.cnet.com/utilities-maintenance/windows/",
        "http://download.cnet.com/utilities-op-systems-updates/windows/",
        "http://download.cnet.com/utilities-other/windows/",
        "http://download.cnet.com/utilities-portable-apps/windows/",
        "http://download.cnet.com/utilities-printer/windows/", "http://download.cnet.com/utilities-sys/windows/",
        "http://download.cnet.com/utilities-uninstallers/windows/", "http://download.cnet.com/video/windows/",
        "http://download.cnet.com/video-dvd-burners/windows/", "http://download.cnet.com/video-dvd-software/windows/",
        "http://download.cnet.com/video-record-capture/windows/", "http://download.cnet.com/video-converters/windows/",
        "http://download.cnet.com/video-editing-production/windows/", "http://download.cnet.com/video-players/windows/",
        "http://download.cnet.com/video-publishing-sharing/windows/"]

for url in urls[246:]:
    opener.get(url)
    # print(opener.page_source)
    text = opener.page_source
    try:
        code = re.search(r'data-category-infinite-scroll-options="(.*?)">', text).group(1)
    except Exception as e:
        print(url)
        continue
    res = unescape(code)
    print(res)
    r = json.loads(res)
    print(r['nodeId'])
    with open("nodes.json", mode='a', encoding='utf-8') as j:
        j.write(r['nodeId']+'\n')
