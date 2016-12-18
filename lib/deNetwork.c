/* ΔOS: Decentralized Operating System

Copyright (c) 2013-2017 Andrew DeSantis <atd@gmx.it>
Copyright (c) 2016-2017 DeSantis Inc. <inc@gmx.it>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

This file incorporates work covered by the BSD 2-Clause License,
as well as the following copyright, and permission notice:

  Copyright (c) 2013-2017 Andrew DeSantis. All rights reserved.
  Copyright (c) 2016-2017 DeSantis Inc. All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions
  are met:

  * Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
  COPYRIGHT HOLDER COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
  OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
  BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
  OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

ΔOS may be used and distributed under the terms of the GPLv3,
which are available at: <http://www.gnu.org/licenses/gpl-3.0.html>

If you would like to embed ΔOS within a commercial application or
redistribute it in a modified binary form, contact DeSantis Inc.
*/

#include "deNetwork.h"

#ifdef __cplusplus
extern "C" {
#endif

#define ENV(key) getenv(key)
#define ENVAR const char *
#define E(s,i) printf("\nErr [%d]: %s\n", i, s)
#define P(s,i) printf("\nOut [%d]: %s\n", i, s)

static int _tcpSocket(int i);
static int _tcpSocket_Error(int i);
static struct sockaddr_in _tcpSocketAddrIn(int port, int i);
static int _tcpBind(int socket_desc, struct sockaddr_in server, int i);
static int _tcpBind_Error(int i);
static void _tcpListen(int socket_desc, int i);
static int _tcpAccept(int socket_desc, int i);
static int _tcpAccept_Error(int i);

int
deZeroTierService(void)
{   ENVAR ZT_PATH = ENV("ZT_PATH");
    ENVAR ZT_NWID = ENV("ZT_NWID");
    zt_start_service(ZT_PATH, ZT_NWID);
    return EXIT_SUCCESS;
}

static int
getPort(void)
{   /*char *filename="/Users/desantis/bitcoin.sh/zerotier/zerotier-one.port";
    FILE *fp = fopen(filename, "rb");
    char *buffer = NULL;
    size_t len;
    ssize_t bytes_read = getdelim(&buffer, &len, '\0', fp);
    if (bytes_read != -1)
        return atoi(buffer);*/
    return atoi("9320");
}

int
deTcpClient(void)
{   printf("client started!\n");
    int port = getPort();
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) printf("could not create socket");
    struct sockaddr_in server;
    server.sin_addr.s_addr = inet_addr("172.29.68.65");
    server.sin_family = AF_INET;
    server.sin_port = htons(port);
    printf("connecting...\n");
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0)
    {   perror("connect failed. Error");
        return EXIT_FAILURE;
    }
    printf("connected\n");
    char *msg = "welcome to the machine!";
    if (send(sock, msg, strlen(msg), 0) < 0)
    {   printf("send failed");
        return EXIT_FAILURE;
    } else {
        printf("sent message: %s\n", msg);
        printf("len = %lu\n", strlen(msg));
    }
    close(sock);
    return EXIT_SUCCESS;
}

int
deTcpServer(void)
{   int index = 0;
    int port = getPort();
    int socket_desc = _tcpSocket(++index); /* socket */
    if (socket_desc == -1) return _tcpSocket_Error(index);
    /* address */
    struct sockaddr_in server = _tcpSocketAddrIn(port, ++index);
    int bind = _tcpBind(socket_desc, server, ++index); /* bind */
    if (pbind < 0) return _tcpBind_Error(index);
    _tcpListen(socket_desc, ++index); /* listen */
    int csoc = _tcpAccept(socket_desc, ++index); /* accept */
    if (csoc < 0) return _tcpAccept_Error(index);
    P("read socket message", ++index); /* repl */
    int msglen = 1024;
    unsigned long count = 0;
    char client_message[2000];
    while (1)
    {   count++;
        int bytes_read = read(csoc, client_message, msglen);
        printf("[%lu] RX = (%d): ", count, bytes_read);
        int i;
        for (i = 0; i < bytes_read; i++)
            printf("%c", client_message[i]);
        int bytes_written = write(csoc, "Server here!", 12);
        printf("\t\nTX = %d\n", bytes_written);
    }
    return EXIT_SUCCESS;
}

static int
_tcpSocket(int i)
{   P("initalize socket", i);
    int s = socket(AF_INET, SOCK_STREAM, 0);
    return s;
}

static int
_tcpSocket_Error(int i)
{   E("couldn't create socket", i);
    return EXIT_FAILURE;
}

static struct sockaddr_in
_tcpSocketAddrIn(int port, int i)
{   P("set socket properties", i);
    struct sockaddr_in server;
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    server.sin_port = htons(port);
    return server;
}

static int
_tcpBind(int socket_desc, struct sockaddr_in server, int i)
{   P("bind socket port", i);
    int pbind = bind(socket_desc,
                     (struct sockaddr *)&server,
                     sizeof(server));
    return pbind;
}

static int
_tcpBind_Error(int i)
{   E("port binding failed", i);
    return EXIT_FAILURE;
}

static void
_tcpListen(int socket_desc, int i)
{   P("listen to socket", i);
    listen(socket_desc, 3);
}

static int
_tcpAccept(int socket_desc, int i)
{   struct sockaddr_in client;
    int c, csoc;
    P("accept socket message", i);
    c = sizeof(struct sockaddr_in);
    csoc = accept(socket_desc,
                 (struct sockaddr *)&client,
                 (socklen_t *)&c);
    return csoc;
}

static int
_tcpAccept_Error(int i)
{   E("accept message failed", i);
    return EXIT_FAILURE;
}

#undef P
#undef E
#undef ENVAR
#undef ENV

#ifdef __cplusplus
}
#endif
