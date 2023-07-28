"""
Personal Photometry Pipeline Configuation File
2016-11-01, mommermiscience@gmail.com
"""

# Photometry Pipeline
# Copyright (C) 2016-2018  Michael Mommert, mommermiscience@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.

# telescope/instrument configurations

# MYTELESCOPE setup parameters
mytelescope_param = {
    'telescope_instrument': 'Telescope/Instrument',  # telescope/instrument name
    'telescope_keyword': 'mytelescope',  # telescope/instrument keyword
    'observatory_code': '695',  # MPC observatory code
    'secpix': (0.1, 0.1),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': True,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('CCDBIN1', 'CCDBIN2'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'g stuff': 'g'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 12,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_default': 3,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/mytelescope.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/mytelescope.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',
    
    # swarp settings
    'copy_keywords': ('OBSERVAT,INSTRUME,EXPTIME,OBJECT,' +
                      'DATE-OBS,TEL_KEYW'),
    #                        keywords to be copied in image
    #                        combination using swarp
    'swarp-config-file': rootpath+'/setup/mytelescope.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['SDSS-R9', 'APASS9', '2MASS']
}

LCO_CPT_EF04_param = {
    'telescope_instrument': 'ef04',  # telescope/instrument name
    'telescope_keyword': 'ef04',  # telescope/instrument keyword
    'observatory_code': 'K93',  # MPC observatory code
    'secpix': (0.341, 0.341),  # pixel size (arcsec) before binning

    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('CCDSUM#blank0', 'CCDSUM#blank1'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),  # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',  # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'gp': 'g',
                            'rp': 'r',
                            'w': 'r',
                            'clear' : 'r'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 5,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 3,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath + '/setup/mytelescope.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # scamp settings
    'scamp-config-file': rootpath + '/setup/lcofli.scamp',
    'reg_max_mag': 19,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['GAIA', 'PANSTARRS', 'SDSS-R9', 'APASS9', '2MASS']
}

# LCOGT, FLI camera (CPT, EF11)
LCO_CPT_EF11_param = {
    # telescope/instrument name
    'telescope_instrument': 'LCOGT(SAAO)/FLI',
    'telescope_keyword': 'LCOFLIEF11',      # telescope/instrument keyword
    'observatory_code': 'K93',         # MPC observatory code
    'secpix': (0.341, 0.341),  # pixel size (arcsec)
    # before binning
    'ext_coeff': 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx': False,
    'flipy': True,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('CCDSUM#blank0', 'CCDSUM#blank1'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',   # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'gp': 'g', 'rp': 'r',
                            'ip': 'i', 'zp': 'z', 'w': 'r' },
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 5,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 3,  # default aperture radius in px
    'aprad_range': [2, 10],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath+'/setup/lcosin.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file': rootpath+'/setup/lcofli.scamp',
    'reg_max_mag': 18,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords': ('TELESCOP,INSTRUME,FILTER,EXPTIME,OBJECT,' +
                      'DATE-OBS,RA,DEC,SECPIX,AIRMASS,' +
                      'TEL_KEYW,MIDTIMJD'),
    #                         keywords to be copied in image
    #                         combination using swarp
    'swarp-config-file': rootpath+'/setup/vatt4k.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'SDSS-R9', 'APASS9']
}

# Las Campanas 1m Swope, Direct CCD camera
swope_param = {
    # telescope/instrument name
    'telescope_instrument': 'LCO(Swope)/CCD',
    'telescope_keyword': 'LCOSWOPE',      # telescope/instrument keyword
    'observatory_code': '304',         # MPC observatory code
    'secpix': (0.435, 0.435),  # pixel size (arcsec)
    # before binning
    'ext_coeff': 0.05,          # typical extinction coefficient


    # image orientation preferences
    'flipx': False,
    'flipy': False,
    'rotate': 0,

    # instrument-specific FITS header keywords
    'binning': ('BINNING#x', 'BINNING#x'),  # binning in x/y
    'extent': ('NAXIS1', 'NAXIS2'),   # N_pixels in x/y
    'ra': 'RA',  # telescope pointing, RA
    'dec': 'DEC',  # telescope pointin, Dec
    'radec_separator': ':',   # RA/Dec hms separator, use 'XXX'
    # if already in degrees
    'date_keyword': 'DATE-OBS',  # obs date/time
    # keyword; use
    # 'date|time' if
    # separate
    'obsmidtime_jd': 'MJD-OBS',  # obs midtime jd keyword
    # (usually provided by
    # pp_prepare
    'object': 'OBJECT',  # object name keyword
    'filter': 'FILTER',  # filter keyword
    'filter_translations': {'g': 'g', 'r': 'r',
                            'i': 'i', 'z': 'z'},
    # filtername translation dictionary
    'exptime': 'EXPTIME',  # exposure time keyword (s)
    'airmass': 'AIRMASS',  # airmass keyword

    # source extractor settings
    'source_minarea': 9,  # default sextractor source minimum N_pixels
    'source_snr': 3,  # default sextractor source snr for registration
    'aprad_default': 5,  # default aperture radius in px
    'aprad_range': [2, 21],  # [minimum, maximum] aperture radius (px)
    'sex-config-file': rootpath+'/setup/swope.sex',
    'mask_file': {},
    #                        mask files as a function of x,y binning

    # registration settings (Scamp)
    'scamp-config-file': rootpath+'/setup/swope.scamp',
    'reg_max_mag': 18,
    'reg_search_radius': 0.5,  # deg
    'source_tolerance': 'high',

    # swarp settings
    'copy_keywords': ('TELESCOP,INSTRUME,FILTER,EXPTIME,OBJECT,' +
                      'DATE-OBS,RA,DEC,AIRMASS,' +
                      'TEL_KEYW,MIDTIMJD'),
    #                         keywords to be copied in image
    #                         combination using swarp
    'swarp-config-file': rootpath+'/setup/vatt4k.swarp',

    # default catalog settings
    'astrometry_catalogs': ['GAIA'],
    'photometry_catalogs': ['PANSTARRS', 'GAIA', 'SDSS-R9', 'APASS9']
}

# add telescope configurations to 'official' telescopes.py

implemented_telescopes.append([ 'LCO-CPT-EF04',
                                'LCO-CPT-EF11',
                                'SWOPE'])

# translate INSTRUME (or others, see _pp_conf.py) header keyword into
#   PP telescope keyword
# example: INSTRUME keyword in header is 'mytel'
instrument_identifiers['ef04'] = 'LCO-CPT-EF04'
instrument_identifiers['ef11'] = 'LCO-CPT-EF11'
instrument_identifiers['Direct/4Kx4K-4'] = 'SWOPE'

### translate telescope keyword into parameter set defined here
telescope_parameters['LCO-CPT-EF04'] = LCO_CPT_EF04_param
telescope_parameters['LCO-CPT-EF11'] = LCO_CPT_EF11_param
telescope_parameters['SWOPE'] = swope_param
