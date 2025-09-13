#!/bin/bash
exec gunicorn app:app --config gunicorn.conf.py
