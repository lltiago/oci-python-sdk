# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WafConfigDetails(object):
    """
    The Web Application Firewall configuration for the WAAS policy creation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new WafConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param access_rules:
            The value to assign to the access_rules property of this WafConfigDetails.
        :type access_rules: list[AccessRule]

        :param address_rate_limiting:
            The value to assign to the address_rate_limiting property of this WafConfigDetails.
        :type address_rate_limiting: AddressRateLimiting

        :param captchas:
            The value to assign to the captchas property of this WafConfigDetails.
        :type captchas: list[Captcha]

        :param device_fingerprint_challenge:
            The value to assign to the device_fingerprint_challenge property of this WafConfigDetails.
        :type device_fingerprint_challenge: DeviceFingerprintChallenge

        :param human_interaction_challenge:
            The value to assign to the human_interaction_challenge property of this WafConfigDetails.
        :type human_interaction_challenge: HumanInteractionChallenge

        :param js_challenge:
            The value to assign to the js_challenge property of this WafConfigDetails.
        :type js_challenge: JsChallenge

        :param origin:
            The value to assign to the origin property of this WafConfigDetails.
        :type origin: str

        :param protection_settings:
            The value to assign to the protection_settings property of this WafConfigDetails.
        :type protection_settings: ProtectionSettings

        :param whitelists:
            The value to assign to the whitelists property of this WafConfigDetails.
        :type whitelists: list[Whitelist]

        """
        self.swagger_types = {
            'access_rules': 'list[AccessRule]',
            'address_rate_limiting': 'AddressRateLimiting',
            'captchas': 'list[Captcha]',
            'device_fingerprint_challenge': 'DeviceFingerprintChallenge',
            'human_interaction_challenge': 'HumanInteractionChallenge',
            'js_challenge': 'JsChallenge',
            'origin': 'str',
            'protection_settings': 'ProtectionSettings',
            'whitelists': 'list[Whitelist]'
        }

        self.attribute_map = {
            'access_rules': 'accessRules',
            'address_rate_limiting': 'addressRateLimiting',
            'captchas': 'captchas',
            'device_fingerprint_challenge': 'deviceFingerprintChallenge',
            'human_interaction_challenge': 'humanInteractionChallenge',
            'js_challenge': 'jsChallenge',
            'origin': 'origin',
            'protection_settings': 'protectionSettings',
            'whitelists': 'whitelists'
        }

        self._access_rules = None
        self._address_rate_limiting = None
        self._captchas = None
        self._device_fingerprint_challenge = None
        self._human_interaction_challenge = None
        self._js_challenge = None
        self._origin = None
        self._protection_settings = None
        self._whitelists = None

    @property
    def access_rules(self):
        """
        Gets the access_rules of this WafConfigDetails.
        The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`, `DETECT`, and `BLOCK` rules, based on different criteria.


        :return: The access_rules of this WafConfigDetails.
        :rtype: list[AccessRule]
        """
        return self._access_rules

    @access_rules.setter
    def access_rules(self, access_rules):
        """
        Sets the access_rules of this WafConfigDetails.
        The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`, `DETECT`, and `BLOCK` rules, based on different criteria.


        :param access_rules: The access_rules of this WafConfigDetails.
        :type: list[AccessRule]
        """
        self._access_rules = access_rules

    @property
    def address_rate_limiting(self):
        """
        Gets the address_rate_limiting of this WafConfigDetails.
        The IP address rate limiting settings used to limit the number of requests from an address.


        :return: The address_rate_limiting of this WafConfigDetails.
        :rtype: AddressRateLimiting
        """
        return self._address_rate_limiting

    @address_rate_limiting.setter
    def address_rate_limiting(self, address_rate_limiting):
        """
        Sets the address_rate_limiting of this WafConfigDetails.
        The IP address rate limiting settings used to limit the number of requests from an address.


        :param address_rate_limiting: The address_rate_limiting of this WafConfigDetails.
        :type: AddressRateLimiting
        """
        self._address_rate_limiting = address_rate_limiting

    @property
    def captchas(self):
        """
        Gets the captchas of this WafConfigDetails.
        A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.


        :return: The captchas of this WafConfigDetails.
        :rtype: list[Captcha]
        """
        return self._captchas

    @captchas.setter
    def captchas(self, captchas):
        """
        Sets the captchas of this WafConfigDetails.
        A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.


        :param captchas: The captchas of this WafConfigDetails.
        :type: list[Captcha]
        """
        self._captchas = captchas

    @property
    def device_fingerprint_challenge(self):
        """
        Gets the device_fingerprint_challenge of this WafConfigDetails.
        The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.


        :return: The device_fingerprint_challenge of this WafConfigDetails.
        :rtype: DeviceFingerprintChallenge
        """
        return self._device_fingerprint_challenge

    @device_fingerprint_challenge.setter
    def device_fingerprint_challenge(self, device_fingerprint_challenge):
        """
        Sets the device_fingerprint_challenge of this WafConfigDetails.
        The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in order to block bots.


        :param device_fingerprint_challenge: The device_fingerprint_challenge of this WafConfigDetails.
        :type: DeviceFingerprintChallenge
        """
        self._device_fingerprint_challenge = device_fingerprint_challenge

    @property
    def human_interaction_challenge(self):
        """
        Gets the human_interaction_challenge of this WafConfigDetails.
        The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.


        :return: The human_interaction_challenge of this WafConfigDetails.
        :rtype: HumanInteractionChallenge
        """
        return self._human_interaction_challenge

    @human_interaction_challenge.setter
    def human_interaction_challenge(self, human_interaction_challenge):
        """
        Sets the human_interaction_challenge of this WafConfigDetails.
        The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page scrolling to identify bots.


        :param human_interaction_challenge: The human_interaction_challenge of this WafConfigDetails.
        :type: HumanInteractionChallenge
        """
        self._human_interaction_challenge = human_interaction_challenge

    @property
    def js_challenge(self):
        """
        Gets the js_challenge of this WafConfigDetails.
        The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.


        :return: The js_challenge of this WafConfigDetails.
        :rtype: JsChallenge
        """
        return self._js_challenge

    @js_challenge.setter
    def js_challenge(self, js_challenge):
        """
        Sets the js_challenge of this WafConfigDetails.
        The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no JavaScript support in order to block bots.


        :param js_challenge: The js_challenge of this WafConfigDetails.
        :type: JsChallenge
        """
        self._js_challenge = js_challenge

    @property
    def origin(self):
        """
        Gets the origin of this WafConfigDetails.
        The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but not on update.


        :return: The origin of this WafConfigDetails.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this WafConfigDetails.
        The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in `Origins`. Required when creating the `WafConfig` resource, but not on update.


        :param origin: The origin of this WafConfigDetails.
        :type: str
        """
        self._origin = origin

    @property
    def protection_settings(self):
        """
        Gets the protection_settings of this WafConfigDetails.
        The settings to apply to protection rules.


        :return: The protection_settings of this WafConfigDetails.
        :rtype: ProtectionSettings
        """
        return self._protection_settings

    @protection_settings.setter
    def protection_settings(self, protection_settings):
        """
        Sets the protection_settings of this WafConfigDetails.
        The settings to apply to protection rules.


        :param protection_settings: The protection_settings of this WafConfigDetails.
        :type: ProtectionSettings
        """
        self._protection_settings = protection_settings

    @property
    def whitelists(self):
        """
        Gets the whitelists of this WafConfigDetails.
        A list of IP addresses that bypass the Web Application Firewall.


        :return: The whitelists of this WafConfigDetails.
        :rtype: list[Whitelist]
        """
        return self._whitelists

    @whitelists.setter
    def whitelists(self, whitelists):
        """
        Sets the whitelists of this WafConfigDetails.
        A list of IP addresses that bypass the Web Application Firewall.


        :param whitelists: The whitelists of this WafConfigDetails.
        :type: list[Whitelist]
        """
        self._whitelists = whitelists

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
