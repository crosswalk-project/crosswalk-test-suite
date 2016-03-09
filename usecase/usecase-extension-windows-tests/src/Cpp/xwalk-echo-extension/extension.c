// Copyright (c) 2016 Intel Corporation. All rights reserved.

#if defined(__cplusplus)
#error "This file is written in C to make sure the C API works as intended."
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "XW_Extension.h"
#include "XW_Extension_SyncMessage.h"

static const char* echo_async_response_prefix = "From dll async:";
static const char* echo_sync_response_prefix = "From dll sync:";

XW_Extension g_extension = 0;
const XW_CoreInterface* g_core = NULL;
const XW_MessagingInterface* g_messaging = NULL;
const XW_Internal_SyncMessagingInterface* g_sync_messaging = NULL;

void instance_created(XW_Instance instance) {
  printf("Instance %d created!\n", instance);
}

void instance_destroyed(XW_Instance instance) {
  printf("Instance %d destroyed!\n", instance);
}

// add a "You said: " prefix to message
static char* build_response(const char* message, const char* echo_ext_response_prefix) {
	int length = strlen(echo_ext_response_prefix) + strlen(message);
	char* response = malloc((length + 1) * sizeof(char));
	strcpy(response, echo_ext_response_prefix);
	strcat(response, message);
	return response;
}

void handle_message(XW_Instance instance, const char* message) {
  char* response = build_response(message, echo_async_response_prefix);
  g_messaging->PostMessage(instance, response);
  free(response);
}

void handle_sync_message(XW_Instance instance, const char* message) {
	char* response = build_response(message, echo_sync_response_prefix);
  g_sync_messaging->SetSyncReply(instance, response);
  free(response);
}

void shutdown(XW_Extension extension) {
  printf("Shutdown\n");
}

int32_t XW_Initialize(XW_Extension extension, XW_GetInterface get_interface) {
  static const char* kAPI =
    "var echoListener = null;"
    "extension.setMessageListener(function(msg) {"
    "  if (echoListener instanceof Function) {"
    "    echoListener(msg);"
    "  };"
    "});"
    "exports.echo = function(msg, callback) {"
    "  echoListener = callback;"
    "  extension.postMessage(msg);"
    "};"
    "exports.syncEcho = function(msg) {"
    "  return extension.internal.sendSyncMessage(msg);"
    "};";

  g_extension = extension;
  g_core = get_interface(XW_CORE_INTERFACE);
  g_core->SetExtensionName(extension, "echo");
  g_core->SetJavaScriptAPI(extension, kAPI);
  g_core->RegisterInstanceCallbacks(
    extension, instance_created, instance_destroyed);
  g_core->RegisterShutdownCallback(extension, shutdown);

  g_messaging = get_interface(XW_MESSAGING_INTERFACE);
  g_messaging->Register(extension, handle_message);

  g_sync_messaging = get_interface(XW_INTERNAL_SYNC_MESSAGING_INTERFACE);
  g_sync_messaging->Register(extension, handle_sync_message);

  return XW_OK;
}
