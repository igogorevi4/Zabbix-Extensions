Prepare php-fpm:

in your pool-config add next lines:

pm.status_path = /php-status
ping.path = /ping 
ping.response = 1


Prepare Nginx:

you need to make another location {} in nginx.conf

location ~ ^/(php-status|ping)$ {
        access_log off;
        allow 127.0.0.1;
        deny all;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
        fastcgi_pass unix:/var/run/php5-fpm.sock;

}

nginx -t  - check errors in nginx.conf
service nginx reload

service php-fpm5 reload


