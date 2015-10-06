
cpe:{part}:{vendor}:{product}:{version}
Part
> The part attribute SHALL have one of these three string values:
- The value “a”, when the WFN is for a class of applications.
- The value “o”, when the WFN is for a class of operating systems.
- The value “h”, when the WFN is for a class of hardware devices.

Vendor
> Values for this attribute SHOULD describe or identify the person or organization that manufactured or created the product. Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification. Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Product
> Values for this attribute SHOULD describe or identify the most common and recognizable title or name of the product. Values for this attribute SHOULD be selected from an attribute-specific valid-values list, which MAY be defined by other specifications that utilize this specification. Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.

Version
> Values for this attribute SHOULD be vendor-specific alphanumeric strings characterizing the particular release version of the product. Version information SHOULD be copied directly (with escaping of printable non-alphanumeric characters as required) from discoverable data and SHOULD NOT be truncated or otherwise modified. Any character string meeting the requirements for WFNs (cf. 5.3.2) MAY be specified as the value of the attribute.
