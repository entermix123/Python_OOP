class PowerCable:
    def connect_device_to_power_outlet(self):       # every power function is removed of inherited classes
        pass


class RCAConnectable:
    def connect_to_device_via_rca_cable(self, device): pass     # every power function is removed of inherited classes


class HDMIConnectable:
    def connect_to_device_via_hdmi_cable(self, device): pass    # every power function is removed of inherited classes


class EthernetCable:
    def connect_by_device_via_ethernet_cable(self, device): pass    # every power function is removed of inherited classes


# class EntertainmentDevice:        # created separated classes for every connection
#     def connect_to_device_via_hdmi_cable(self, device): pass
#     def connect_to_device_via_rca_cable(self, device): pass
#     def connect_to_device_via_ethernet_cable(self, device): pass
#     def connect_device_to_power_outlet(self, device): pass


class Television(HDMIConnectable, PowerCable):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_hdmi_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)


class DVDPlayer(PowerCable, HDMIConnectable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)


class GameConsole(HDMIConnectable, EthernetCable, PowerCable):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_by_device_via_ethernet_cable(router)


class Router(EthernetCable, PowerCable):
    def connect_to_tv(self, television):
        self.connect_by_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_by_device_via_ethernet_cable(game_console)
