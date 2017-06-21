#!/bin/bash

DB_NAME=$1

TEMPLATE='postgresql.DATABASENAME.xml'

DB_TEMPLATE=postgresql.$DB_NAME.xml

cp $TEMPLATE $DB_TEMPLATE

sed -i "s/DATABASENAME/$DB_NAME/g" $DB_TEMPLATE

