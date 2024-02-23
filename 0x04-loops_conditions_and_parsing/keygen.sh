#!/usr/bin/env bash
# This script generates an RSA key pair with custom filenames

# Define filenames
private_key_file="0-RSA_public_key"
public_key_file="0-RSA_public_key.pub"

# Generate RSA key pair
ssh-keygen -t rsa -b 4096 -f "$private_key_file" -N ""

# Rename private_key_file
mv 0-RSA_public_key RSA_private_key
renamed_private_key_file="RSA_private_key"

# Display success message
echo "RSA key pair generated successfully."
echo "Public key saved to $public_key_file."
echo "Private key saved to $renamed_private_key_file (no passphrase)."

