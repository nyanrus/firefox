# nsIEnterprisePolicies (toolkit/components/enterprisepolicies/nsIEnterprisePolicies.idl)

source: toolkit/components/enterprisepolicies/nsIEnterprisePolicies.idl
source-hash: 431bcd74b55d604b747c3097520bd14138651874

- 継承: nsISupports
- 役割: (未記入)
- 実装: `policies` (toolkit/components/enterprisepolicies/components.conf)
- contract ID: `@mozilla.org/enterprisepolicies;1`
- 使っているJS: [`browser/components/preferences/config/search.mjs`](../../../browser/components/preferences/config/search.mjs.md), [`browser/components/shell/StartupOSIntegration.sys.mjs`](../../../browser/components/shell/StartupOSIntegration.sys.mjs.md)

## メソッド / 属性
- `const short UNINITIALIZED`: (未記入)
- `const short INACTIVE`: (未記入)
- `const short ACTIVE`: (未記入)
- `const short FAILED`: (未記入)
- `readonly attribute short status`: (未記入)
- `readonly attribute boolean isEnterprise`: (未記入)
- `boolean isAllowed(ACString feature)`: Checks if a specific feature is allowed by the enterprise policies.
- `boolean isAllowedForURI(ACString feature, nsIURI uri)`: Checks if a specific feature is allowed for a given URI by the enterprise
- `jsval getActivePolicies()`: Get the active policies that have been successfully parsed.
- `jsval getSupportMenu()`: Get the contents of the support menu (if applicable)
- `jsval getExtensionPolicy(ACString extensionID)`: Get the policy for a given extensionID (if available)
- `jsval getExtensionSettings(ACString extensionID)`: Retrieves the ExtensionSettings policy for the given extensionID.
- `boolean mayInstallAddon(jsval addon)`: Uses the allowlist, blocklist and settings to determine if an addon
- `boolean isAddonRequiredByPolicy(ACString addonID)`: Checks whether an enterprise policy requires the given addon to be
- `boolean allowedInstallSource(nsIURI uri)`: Uses install_sources to determine if an addon can be installed
- `boolean isExemptExecutableExtension(ACString url, ACString extension)`: Uses ExemptDomainFileTypePairsFromFileTypeDownloadWarnings to determine
- `unsigned long getContainerForURI(nsIURI uri)`: Returns the userContextId of the container that a navigation to the given
