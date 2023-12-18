from .locales import Translator as langT

_ = langT('translator_toEnglish', 'en').lang.gettext

class Translator:
    names = {'depth': _('Maxdjup i plot (m)'),
             'bin_size': _('Djupgrid (m)'),
             'cruise': _('Expedition nr'),
             'vessel': _('Fartyg'),
             'series': _('Serie'),
             'tail': _('Testkast'),
             'station': _('Station'),
             'distance': _('Avstånd till station (m)'),
             'operator': _('CTD operatör'),
             'position': _('Position'),
             'event_id': _('EventID      '),
             'parent_event_id': _('ParentEventID'),

             'mprog':   _('Övervakningsprogram'),
             'proj':    _('Projekt'),
             'orderer': _('Beställare'),
             'slabo':   _('Provtagande laboratorium'),
             'alabo':   _('Analyserande laboratorium'),
             'refsk':   _('Provtagningsmetod referens'),

             'wadep_bot': _('Bottendjupet ska vara [m]'),
             'wadep': _('Ekolodsdjup vid station [m]'),
             'windir': _('Vindriktning'),
             'winsp': _('Vindhastighet [m/s]'),
             'airtemp': _('Lufttemperatur [grader C]'),
             'airpres': _('Lufttryck [hPa]'),
             'weath': _('Väder [kod]'),
             'cloud': _('Moln [kod]'),
             'waves': _('Vågor [kod]'),
             'iceob': _('Is [kod]'),
             'comment': _('CTD kommentar')}

    def __init__(self):
        self.reversed_names = {value: key for key, value in self.names.items()}

    def get_readable(self, item):
        return self.names.get(item, item)

    def get_id(self, item):
        return self.reversed_names.get(item, item)