# Jailbreak status checker

This is a very simple checker that uses the [*Can I Jailbreak?* API](https://canijailbreak.com/) to see if the latest version of iOS has a jailbreak. Run `jailbreakstatus`. Exit code `0` means yes and `1` means no.

```sh
jailbreakstatus && sendmail me@me.com <<< 'Latest iOS is jailbreakable'
```
