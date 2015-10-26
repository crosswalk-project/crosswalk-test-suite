package org.xwalk.embedded.api.asyncsample.misc;

import org.json.JSONObject;
import org.xwalk.core.XWalkExtension;

import android.app.Activity;
import android.content.ContentUris;
import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.net.Uri;
import android.provider.ContactsContract;
import android.provider.ContactsContract.CommonDataKinds.Phone;
import android.provider.ContactsContract.CommonDataKinds.StructuredName;
import android.provider.ContactsContract.Contacts.Data;
import android.provider.ContactsContract.RawContacts;
import android.util.Log;

public class ExtensionContact extends XWalkExtension{
    final private static String TAG = "ExtensionContact";
    private Context mContext = null;

	public ExtensionContact(Context context) {
        super("contact",
                "var readCallback = null;"
                + "extension.setMessageListener(function(phone) {"
                + "  if (readCallback instanceof Function) {"
                + "    readCallback(phone);"
                + "  };"
                + "});"
                + "exports.read = function(name, callback) {"
                + "  readCallback = callback;"
                + "  extension.postMessage(JSON.stringify({\"cmd\":\"read\", \"name\":name}));"
                + "};"
                + "exports.write = function(name, phone) {"
                + "  return extension.postMessage(JSON.stringify({\"cmd\": \"write\", \"name\": name, \"phone\": phone}));"
                + "};"
               );
		mContext = context;
	}

	@Override
	public void onMessage(int instanceID, String message) {
		// TODO Auto-generated method stub
        try {
            JSONObject m = new JSONObject(message);
            String cmd = m.getString("cmd");
            String name = m.getString("name");
            if (cmd.equals("read")) {
                String storedPhone = "";
                try {
                    storedPhone = readContact(name);
                } catch (Exception e) {
                    Log.e(TAG, "Failed to read phone number for name=" + name);
                    Log.e(TAG, e.toString());
                    e.printStackTrace();
                }
                postMessage(instanceID, storedPhone);

            } else if (cmd.equals("write")) {
                String phone = "";
                try {
                    phone = m.getString("phone");
                    writeContact(name, phone);
                } catch (Exception e) {
                    Log.e(TAG, "Failed to write contact, name=" + name + ", phone=" + phone);
                    Log.e(TAG, e.toString());
                    e.printStackTrace();
                }
            } else {
                Log.e(TAG, "Unsupported command: " + cmd);
            }
        } catch(Exception e) {
            Log.e(TAG, "Invalid message: " + message);
            Log.e(TAG, e.toString());
            e.printStackTrace();
            return;
        }
	}

	@Override
	public String onSyncMessage(int arg0, String arg1) {
		// TODO Auto-generated method stub
		return null;
	}

    String readContact(String name) {
        Activity cActivity = (Activity) mContext;
        // find the contacts by name
        Cursor cursor = cActivity.getContentResolver().query(
                ContactsContract.Contacts.CONTENT_URI, null,
                ContactsContract.Contacts.DISPLAY_NAME + "='" + name + "'",
                null, null);
        if (cursor.moveToNext()) {
            // get the first phone of the specified name
            Cursor phones = cActivity.getContentResolver().query(
                    ContactsContract.CommonDataKinds.Phone.CONTENT_URI,
                    null,
                    ContactsContract.Contacts.DISPLAY_NAME + "='" + name + "'",
                    null, null);

            if (phones.moveToNext()) {
                String phone = phones.getString(phones.getColumnIndex(ContactsContract.CommonDataKinds.Phone.NUMBER));
                phones.close();
                cursor.close();
                return phone;
            } else {
                Log.w(TAG, "no phone number for " + name);
                cursor.close();
                return "";
            }
        } else {
            Log.e(TAG, "no such person named:" + name);
            return "";
        }
    }

    void writeContact(String name, String phone) {
        //get Android context
        Activity cActivity = (Activity) mContext;
        ContentValues values = new ContentValues();

        Uri rawContactUri = cActivity.getContentResolver().insert(RawContacts.CONTENT_URI, values);
        long rawContactId = ContentUris.parseId(rawContactUri);
        values.put(Data.RAW_CONTACT_ID, rawContactId);

        values.put(Data.MIMETYPE, StructuredName.CONTENT_ITEM_TYPE);

        values.put(StructuredName.GIVEN_NAME, name);

        cActivity.getContentResolver().insert(android.provider.ContactsContract.Data.CONTENT_URI, values);
        values.clear();
        values.put(Data.RAW_CONTACT_ID, rawContactId);
        values.put(Data.MIMETYPE, Phone.CONTENT_ITEM_TYPE);

        values.put(Phone.NUMBER, phone);

        values.put(Phone.TYPE, Phone.TYPE_MOBILE);

        cActivity.getContentResolver().insert(android.provider.ContactsContract.Data.CONTENT_URI, values);
    }

}
