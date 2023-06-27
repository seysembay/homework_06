#!/usr/bin/env bash

echo "Run migrations"
#flask db stamp head
flask db upgrade
