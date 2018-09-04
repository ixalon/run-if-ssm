# run-if-ssm

This utility allows you to conditionally run a command based on the value of an AWS SSM Parameter

## Usage

```
usage: run-if-ssm [-h] [--param PARAM] [--region AWS_REGION]
                  [--profile AWS_PROFILE] [--value VALUE]
                  [--condition CONDITION] [--not] [--with-decryption]
                  [--set-on-success SET_ON_SUCESS] [--default-value DEFAULT]
                  [--delete-on-success] [--verbose]
                  [COMMAND [COMMAND ...]]

Runs an arbitrary command if an AWS SSM parameter meets a given condition.

positional arguments:
  COMMAND               Command to run (default: -)

optional arguments:
  -h, --help            show this help message and exit
  --param PARAM         Name of SSM parameter to read (default: -)
  --region AWS_REGION   AWS region in which the ECS cluster resides (default:
                        -)
  --profile AWS_PROFILE
                        AWS profile to use (default: -)
  --value VALUE         Value to compare against (default: -)
  --condition CONDITION
                        Condition to compare value with (default: 'equals')
  --not                 Negate the condition (default: False)
  --with-decryption     Decrypt value before comparison (default: False)
  --set-on-success SET_ON_SUCESS
                        Value to set the SSM parameter to on success (default:
                        -)
  --default-value DEFAULT
                        Value to use if SSM paramter is missing (default: -)
  --delete-on-success   Delete the SSM paramter if the command returns
                        successfully (default: False)
  --verbose             Output debug information (default: False)
```

