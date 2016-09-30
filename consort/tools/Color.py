# -*- encoding: utf-8 -*-
import colorsys
from abjad.tools import abctools


class Color(abctools.AbjadValueObject):
    r'''An RGB color.

    ::

        >>> import consort
        >>> color = consort.Color(1.0, 0.92, 0.8)
        >>> print(format(color))
        consort.tools.Color(
            red=1.0,
            green=0.92,
            blue=0.8,
            )

    ::

        >>> print(format(color, 'lilypond'))
        #(rgb-color 1.0 0.92 0.8)

    ::

        >>> color.hls
        (0.1..., 0.9, 1.0)

    ::

        >>> color.with_saturation(0.5)
        Color(red=0.95, green=0.91, blue=0.85...)

    ::

        >>> color.rotate_hue(0.25)
        Color(red=0.8, green=1.0, blue=0.82)

    ::

        >>> color.scale_luminance(1)
        Color(red=1.0, green=0.95..., blue=0.89...)

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_red',
        '_green',
        '_blue',
        )

    _x11_colors = {
        'Lavender': (90, 90, 98),
        }

    ### INITIALIZER ###

    def __init__(self, red=1.0, green=1.0, blue=1.0):
        red = float(red)
        green = float(green)
        blue = float(blue)
        assert 0. <= red <= 1.0
        assert 0. <= green <= 1.0
        assert 0. <= blue <= 1.0
        self._red = red
        self._green = green
        self._blue = blue

    ### SPECIAL METHODS ###

    def __format__(self, format_specification=''):
        from abjad.tools import systemtools
        if format_specification in ('', 'storage'):
            return systemtools.StorageFormatAgent(self).get_storage_format()
        elif format_specification == 'lilypond':
            return self._lilypond_format
        return str(self)

    ### PRIVATE PROPERTIES ###

    @property
    def _lilypond_format(self):
        return '#(rgb-color {:.03} {:.03} {:.03})'.format(
            self.red,
            self.green,
            self.blue,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def from_hls(cls, hue, luminance, saturation):
        red, green, blue = colorsys.hls_to_rgb(hue, luminance, saturation)
        return cls(red=red, green=green, blue=blue)

    @classmethod
    def from_x11(cls, name):
        r, g, b = cls._x11_colors[name]
        return cls(r / 100., g / 100., b / 100.)

    def rotate_hue(self, rotation):
        hue, luminance, saturation = self.hls
        hue += float(rotation)
        hue %= 1.0
        return self.from_hls(hue, luminance, saturation)

    def scale_saturation(self, scale):
        scale = 2.0 ** float(-scale)
        hue, luminance, saturation = self.hls
        saturation **= scale
        return self.from_hls(hue, luminance, saturation)

    def scale_luminance(self, scale):
        scale = 2.0 ** float(-scale)
        hue, luminance, saturation = self.hls
        luminance **= scale
        return self.from_hls(hue, luminance, saturation)

    def with_hue(self, hue):
        hue = float(hue)
        assert 0. <= hue <= 1.
        _, luminance, saturation = self.hls
        return self.from_hls(hue, luminance, saturation)

    def with_luminance(self, luminance):
        luminance = float(luminance)
        assert 0. <= luminance <= 1.
        hue, _, saturation = self.hls
        return self.from_hls(hue, luminance, saturation)

    def with_saturation(self, saturation):
        saturation = float(saturation)
        assert 0. <= saturation <= 1.
        hue, luminance, _ = self.hls
        return self.from_hls(hue, luminance, saturation)

    ### PUBLIC PROPERTIES ###

    @property
    def blue(self):
        return self._blue

    @property
    def green(self):
        return self._green

    @property
    def hue(self):
        return self.hls[0]

    @property
    def hls(self):
        return colorsys.rgb_to_hls(self.red, self.green, self.blue)

    @property
    def luminance(self):
        return self.hls[1]

    @property
    def red(self):
        return self._red

    @property
    def rgb(self):
        return self.red, self.green, self.blue

    @property
    def saturation(self):
        return self.hls[2]
